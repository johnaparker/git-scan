# Git-Scan
Git-Scan is a command-line utility to scan local or remote git repositories for history that is divergent from the remote branch.
It is particularly useful when dealing with multiple git repositories across multiple machines where pulls and pushes are missed, stashes are forgotten about, files are left untracked, etc.

## Features
+ Scan repositories for missing push & pulls, uncommited changes, untracked files, leftover stashes, and dangling branches
+ Automatically pull or push a group of repositories
+ Execute over SSH to git-scan on a different computer
+ Open repositories in need of changes in TMUX windows (including over SSH)
+ Configuration file to list scannable repositories and remote SSH hosts

## Usage
To run a git-scan
```
git-scan [--push] [--pull] [--repo] [--tmux] [--ssh]
```
where the optional arguments are
+ **``push:``**   push repository changes if ahead of remote
+ **``pull:``**   pull repository changes if behind remote and there are no merge conflicts
+ **``repo:``**   list of repositories to scan (defaults to all in the configuration file)
+ **``tmux:``**   open all repositories with problems to fix in a TMUX window
+ **``ssh:``**    run the git-scan on the provided ssh host

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
git-scan list [--resolve]
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

## Configuration File
A configuration file located at ``~/.config/git-scan/git-scan.conf`` is created.
This is a TOML file listing the scannable repositories and remote hosts:
```
repositories = ["/path/to/repository_1", "/path/to/repository_2"]
ssh = ["host1", "host2"]
```
The config file can be editted manually or changed using the ``add`` and ``remove`` commands.
Glob patterns and tilde expansions are allowed, i.e. ``"~/path/to/repos/*"``

## License
Git-Scan is licensed under the terms of the MIT license.
