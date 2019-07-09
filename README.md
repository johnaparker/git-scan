# Git-Scan
Git-Scan is a command-line utility to scan local or remote git repositories for history that is divergent from the remote branch

## Features
+ Scan repositories for missing push & pulls, uncommited changes, untracked files, leftover stashes, and dangling branches
+ Automatically pull or push a group of repositories
+ Execute over SSH to git-scan on a different computer
+ Open repositories in need of changes in TMUX windows (including over SSH)
+ Configuration file to list scannable repositories and remote SSH hosts

## Usage
To run a git-scan
```
git-scan [--tmux] [--ssh] [--push] [--pull] [--repo]
```
To add a repository to the list of scannable repositories
```
git-scan add /path/to/repository
```
To remove a repository
```
git-scan remove /path/to/repository
```
To list all scannable repositories
```
git-scan list
```

## Installation
Clone the repository
```shell
git clone https://github.com/johnaparker/git-scan.git && cd git-scan
```
and install with pip
```shell
pip install .
```
If installed with the ``--user`` flag, make sure to add ``~/.local/bin`` to your PATH

## License
Git-Scan is licensed under the terms of the MIT license.
