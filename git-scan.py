import subprocess
from termcolor import colored
import toml
import argparse
import enum

"""
Configuration can be used to control which ones are checked (default: all)
Checks should be applied to every branch
tmux option to open projects in window -- auto-show diff, etc.
option to pull all and report on errors

testing: create temp repo
TOML config file: list git paths; list remotes
argparse to: list projects, display changes, perform action, open tmux

learn: setup.py for a project that installs a bin file
learn: to execute everything over ssh

detect all git repos within a repo as part of config (but not submodules?)
add (optional) groups for groups of repos

see related project: https://github.com/totten/git-scan
see creating git command: https://github.com/rotati/wiki/wiki/Create-custom-Git-command
                          https://dev.to/shobhit/git-refresh-4hn
"""

class History(enum.Enum):
    EQUAL    = enum.auto()  # history is the same as remote
    PULL     = enum.auto()  # history is behind remote
    PUSH     = enum.auto()  # history is ahead of remote
    DIVERGED = enum.auto()  # history has diverged from remote

paths = ['/home/john/projects/miepy',
         '/home/john/projects/stoked']

def run_git_command(options, git_path):
    """Run a git command
    
    Arguments:
        options    list of commands following git
        git_path   path to git repository
    """
    cmd = subprocess.Popen(['git',] + list(options), stdout=subprocess.PIPE, cwd=git_path)
    text = cmd.communicate()[0].decode()
    return text

def git_diff(git_path):
    """run git diff"""
    return run_git_command(['diff'], git_path)

def git_fetch(git_path):
    """run git fetch"""
    return run_git_command(['fetch'], git_path)

def local_sha(git_path):
    """get the local SHA"""
    return run_git_command(['rev-parse', '@'], git_path).strip()

def remote_sha(git_path):
    """get the remote SHA"""
    return run_git_command(['rev-parse', '@{u}'], git_path).strip()

def base_sha(git_path):
    """get the remote base SHA"""
    return run_git_command(['merge-base', '@', '@{u}'], git_path).strip()

def git_untracked_files(git_path):
    """get untracked files"""
    return run_git_command(['ls-files', '--others', '--exclude-standard'], git_path)

def get_history(git_path, fetch=True):
    """Obtain the status of the history relative to the remote

    Arguments:
        git_path   path to git repository
        fetch      (bool) If True, fetch remote data before getting history
    """
    if fetch:
        git_fethc(git_path)

    local = local_sha(git_path)
    remote = remote_sha(git_path)
    base = base_sha(git_path)

    if local == remote:
        return History.EQUAL
    elif local == base:
        return History.PULL
    elif remote == base:
        return History.PUSH
    else:
        return History.DIVERGED

for path in paths:
    diff_text = git_diff(path)
    history = get_history(path)
    untracked = git_untracked_files(path)

    ### un-commited branches

    ### stashes



    ### display
    print(colored(path, color='yellow'))
    if diff_text:
        print('\tdiffs')
    if history != history.EQUAL:
        print('\t' + str(history))
    if untracked:
        print('\tuntracked files')
    print()
