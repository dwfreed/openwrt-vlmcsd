#!/usr/bin/env python3

# run this from within a full, up-to-date, clone of openwrt.git
# (then copy matrix.json back to this dir)
# note that running this will checkout various tags and leave you somewhere else than you were

from bs4 import BeautifulSoup # Don't ask...
import json
import requests
import sh
import sh.contrib

class OpenWrtVersionSort:
    def __init__(self, tag):
        ver, _, rc = tag.partition('-rc')
        major, _, minor = ver.rpartition('.')
        self.major = major
        self.minor = int(minor)
        if rc:
            self.rc = int(rc)
        else:
            self.rc = None
        pass
    def __lt__(self, other):
        return self.compare(self, other) < 0
    def __gt__(self, other):
        return self.compare(self, other) > 0
    def __eq__(self, other):
        return self.compare(self, other) == 0
    def __le__(self, other):
        return self.compare(self, other) <= 0
    def __ge__(self, other):
        return self.compare(self, other) >= 0
    def __ne__(self, other):
        return self.compare(self, other) != 0

    @staticmethod
    def compare(a, b):
        if a.major > b.major:
            return 1
        elif a.major < b.major:
            return -1
        elif a.minor > b.minor:
            return 1
        elif a.minor < b.minor:
            return -1
        elif a.rc is None and b.rc is not None:
            return 1
        elif a.rc is not None and b.rc is None:
            return -1
        else:
            return a.rc - b.rc


dump_target_info = sh.Command('scripts/dump-target-info.pl')

sh.contrib.git.fetch('--tags')

git_tags = sh.contrib.git.tag().split('\n')
git_tags = [tag[1:] for tag in git_tags if tag.startswith('v')]
majors = sorted({'.'.join(tag.split('.')[:2]) for tag in git_tags})
majors = majors[-3:]
tags = [sorted([tag for tag in git_tags if major in tag], key=OpenWrtVersionSort)[-1] for major in majors]

matrix = []
for major, tag in zip(majors, tags):
    sh.contrib.git.checkout(f'v{tag}')

    for line in dump_target_info.architectures().split('\n'):
        if not line:
            continue

        arch, _, targets_str = line.partition(' ')

        for target in targets_str.split(' '):
            url = f'https://downloads.openwrt.org/releases/{tag}/targets/{target}/'

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            sdk = ''
            for link in soup.find_all('a'):
                if not link['href']:
                    continue

                if 'openwrt-sdk' not in link['href']:
                    continue

                sdk = link['href']
                break

            if sdk:
                break

        else:
            print(f'SDK not found for {tag} {arch} {targets_str}!')
            continue

        job = {
                'major': major,
                'tag': tag,
                'arch': arch,
                'sdk_url': f'{url}/{sdk}',
                'sdk_filename': sdk,
        }
        matrix.append(job)

json.dump(matrix, open('matrix.json', 'w'))
