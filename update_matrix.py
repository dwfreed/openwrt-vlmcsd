#!/usr/bin/env python3

from bs4 import BeautifulSoup # Don't ask...
import json
import requests
import sh
import sh.contrib

dump_target_info = sh.Command('scripts/dump-target-info.pl')

sh.contrib.git.fetch('--tags')

git_tags = sh.contrib.git.tag().split('\n')
git_tags = [tag[1:] for tag in git_tags if tag.startswith('v')]
majors = sorted({'.'.join(tag.split('.')[:2]) for tag in git_tags})
majors = majors[-2:]
tags = [sorted([tag for tag in git_tags if major in tag])[-1] for major in majors]

matrix = []
for major, tag in zip(majors, tags):
    sh.contrib.git.checkout(f'v{tag}')

    for line in dump_target_info.architectures().split('\n'):
        if not line:
            continue

        arch, _, targets_str = line.partition(' ')
        target, _, __ = targets_str.partition(' ')

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

        if not sdk:
            print(f'SDK not found for {tag} {arch} {target}!')
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
