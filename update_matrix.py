#!/usr/bin/env python3

# run this from within a full, up-to-date, clone of openwrt.git
# (then copy matrix.json back to this dir)
# note that running this will checkout various tags and leave you somewhere else than you were

from bs4 import BeautifulSoup # Don't ask...
import json
import requests
import sh
import sh.contrib

class OpenWrtVersion:
    def __init__(self, tag):
        ver, _, rc = tag.partition('-rc')
        year, month, minor = ver.split('.')
        self.year = int(year)
        self.month = int(month)
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

    def __str__(self):
        if self.rc:
            return f'{self.year}.{self.month:02d}.{self.minor}-rc{self.rc}'
        else:
            return f'{self.year}.{self.month:02d}.{self.minor}'

    def major(self):
        return f'{self.year}.{self.month:02d}'

    @staticmethod
    def compare(a, b):
        if a.year != b.year:
            return a.year - b.year
        elif a.month != b.month:
            return a.month - b.month
        elif a.minor != b.minor:
            return a.minor - b.minor
        elif a.rc is None and b.rc is not None:
            return 1
        elif a.rc is not None and b.rc is None:
            return -1
        else:
            return a.rc - b.rc


try:
    dump_target_info = sh.Command('scripts/dump-target-info.pl')
except:
    dump_target_info = None

sh.contrib.git.fetch('--tags')

git_tags = sh.contrib.git.tag().split('\n')
versions = [OpenWrtVersion(tag[1:]) for tag in git_tags if tag.startswith('v')]
majors = sorted({version.major() for version in versions}, reverse=True)
versions_by_major = {major: sorted([version for version in versions if version.major() == major], reverse=True) for major in majors}

keep_majors = 2
if versions_by_major[majors[0]][0].rc:
    keep_majors += 1
majors = majors[:keep_majors]

matrix = []
major_arches_done = set()
major_arches_seen = {}
for major in majors:
    print(f'Starting major {major}')
    for version in versions_by_major[major]:
        if version.rc and not versions_by_major[major][0].rc:
            break

        print(f' Starting version {version}')

        sh.contrib.git.checkout(f'v{version}')

        if not dump_target_info:
            try:
                dump_target_info = sh.Command('scripts/dump-target-info.pl')
            except:
                dump_target_info = None
                print(f'  Version {version} unavailable due to missing target info script')
                continue

        try:
            dump_target_info_lines = dump_target_info.architectures().split('\n')
        except:
            print(f'  Version {version} unavailable due to missing target info script')
            continue

        for line in dump_target_info_lines:
            if not line:
                continue

            arch, _, targets_str = line.partition(' ')

            if f'{major}-{arch}' in major_arches_done:
                continue

            versions_seen = major_arches_seen.setdefault(f'{major}-{arch}', list())
            versions_seen.append(str(version))

            print(f'  Starting arch {arch}')

            for target in targets_str.split(' '):
                print(f'   Trying target {target}: ', end='', flush=True)

                url = f'https://downloads.openwrt.org/releases/{version}/targets/{target}/'

                response = requests.get(url)

                soup = BeautifulSoup(response.text, 'html.parser')

                sdk = ''
                for link in soup.find_all('a'):
                    if not link['href']:
                        continue

                    if 'openwrt-sdk' not in link['href']:
                        continue

                    sdk = link['href']
                    print('found')
                    break

                if sdk:
                    break
                else:
                    print('not found')

            else:
                continue

            job = {
                    'major': major,
                    'tag': str(version),
                    'arch': arch,
                    'sdk_url': f'{url}/{sdk}',
                    'sdk_filename': sdk,
            }
            matrix.append(job)
            major_arches_done.add(f'{major}-{arch}')

major_arches_missed = set(major_arches_seen.keys()) - major_arches_done
if major_arches_missed:
    print("An SDK was never found for the following major-arch combos, listed with the versions they were seen in: (note that some arches may be source-only; check upstream openwrt to see)")
    for major_arch in major_arches_missed:
        print(f'{major_arch}:', *major_arches_seen[major_arch])

json.dump(matrix, open('matrix.json', 'w'))
