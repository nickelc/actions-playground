'''Utilities for GitHub Actions'''

import os
import shutil
import subprocess
from contextlib import contextmanager

def get_input(name, default=''):
    '''Gets the value of an input. The value is also trimmed.'''
    name = name.replace(' ', '_').upper()
    try:
        value = os.environ['INPUT_' + name]
        return value.strip()
    except KeyError:
        return default

@contextmanager
def group(title):
    '''
    Return a context manager that creates an expandable group in logs.

    Example:
        with group('My Title'):
            print('Inside group')

    Output:
        ::group::My Title
        Inside group
        ::endgroup::
    '''
    try:
        print('::group::' + title)
        yield
    finally:
        print('::endgroup::')

def debug(message):
    '''Prints a debug message to the log.'''
    print('::debug::' + message)

def set_output(name, value):
    '''Sets the action's output parameter'''
    print('::set-output name={}::{}'.format(name, value))

def execute(cmd, args):
    '''Execute a command'''
    cmd = shutil.which(cmd)
    print('[command]' + cmd + ' ' +  ' '.join(args), flush=True)
    subprocess.run([cmd, *args])
