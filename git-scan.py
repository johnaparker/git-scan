import subprocess
from termcolor import colored
import toml
import argparse
"""
Write each check below as independent function
Configuration can be used to control which ones are checked (default: all)
Checks should be applied to every branch
tmux option to open projects in window -- auto-show diff, etc.
option to pull all and report on errors

testing: create temp repo
TOML config file: list git paths; list remotes
argparse to: list projects, display changes, perform action, open tmux

learn: setup.py for a project that installs a bin file
learn: to execute everything over ssh

detect all git repos within a folder as part of config (but not submodules?)

see related project: https://github.com/totten/git-scan
see creating git command: https://github.com/rotati/wiki/wiki/Create-custom-Git-command
                          https://dev.to/shobhit/git-refresh-4hn
"""

paths = ['/home/john/projects/miepy',
         '/home/john/projects/stoked']

for path in paths:
    ### check for uncommitted changes
    diff = subprocess.Popen(('git', 'diff'), stdout=subprocess.PIPE, cwd=path)
    diff_text = diff.communicate()[0].decode()

    ### check for missing pull/push

    ### check for uncommitted files

    ### un-commited branches

    ### stashes



    ### display
    print(colored(path, color='yellow'))
    if diff_text:
        print('\tdiffs')
    print()
