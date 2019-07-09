Git_-Scan
==============
Git-Scan scans local or remote git repositories for history that is divergent from the origin branch.

Features
--------------
+ Scan repositories for missing push/pulls, uncommited changes, untracked files, stashes, and dangling branches
+ Automatically pull or push a group of repositories
+ Open repositories in need of changes in TMUX windows
+ Execute over SSH to git-scan on a different computer
+ Configuration file to list repositories and remote SSH hosts

Usage
--------------
git-scan [--tmux] [--ssh] [--push] [--pull] [--repo]

Installation
--------------
Clone the repository
```shell
git clone https://github.com/johnaparker/git-scan.git && cd git-scan
```
and install with pip
```shell
pip install .
```
If installed with the ``--user`` flag, make sure to add ~/.local/bin to your PATH

License
--------------
MiePy is licensed under the terms of the MIT license.
