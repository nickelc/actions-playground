#!/usr/bin/env python

import os, subprocess

def to_list(s):
    return [x for x in map(str.strip, s.split(',')) if len(x) > 0]

toolchain = os.environ.get('INPUT_TOOLCHAIN', 'stable')

targets = os.environ.get('INPUT_TARGETS', '')
targets = ['-t', *to_list(targets)]

components = os.environ.get('INPUT_COMPONENTS', '')
components = ['-c', *to_list(components)]

subprocess.run(['rustup', 'self', 'update'])
subprocess.run(['rustup', 'set', 'profile', 'minimal'])

args = ['rustup', 'toolchain', 'install', toolchain, *targets, *components]

print(args)
