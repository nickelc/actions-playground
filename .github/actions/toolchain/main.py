#!/usr/bin/env python3
'''Rust toolchain installer'''

import re
import subprocess
from actions import get_input, set_output, group, execute

VERSION = re.compile(r'\S+\s((\S+)\s\((?:(\S+)\s)?(\S+)\))')

def to_list(value):
    '''Return a list of words in a comma-separated string.'''
    return [x for x in map(str.strip, value.split(',')) if len(x) > 0]

def get_version(args):
    '''Return a version tuple from the process output'''
    output = subprocess.check_output(args).decode('utf-8')
    m = VERSION.match(output)
    return m.group(1, 3) if m else (None, None)

toolchain = get_input('toolchain', 'stable')

targets = to_list(get_input('targets'))
targets = ['-t', *targets] if len(targets) > 0 else []

components = to_list(get_input('components'))
components = ['-c', *components] if len(components) > 0 else []

execute('rustup', ['self', 'update'])
execute('rustup', ['set', 'profile', 'minimal'])

execute('rustup', ['toolchain', 'install', toolchain, *targets, *components])

with group('Gathering version information'):
    version, hash_s = get_version(['rustc', '-V'])
    if version:
        set_output('rustc', version)
        if hash_s:
            set_output('rustc_hash', hash_s)

    version, _ = get_version(['cargo', '-V'])
    if version:
        set_output('cargo', version)

    version, _ = get_version(['rustup', '-V'])
    if version:
        set_output('rustup', version)
