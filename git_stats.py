import pandas as pd
from git import Repo
import subprocess
from glob import glob

usernames = pd.read_csv('./names.txt', delim_whitespace=True, header=0, index_col=0)


commits_rec = []
branch_rec = []
lines_rec = []
pynb_lines_rec = []
pynb_rec = []
py_rec = []

direc = 'hw5'
rsa = '262eecbd5'
filename = 'HeatEquationFourier.ipynb'
init_commits = 2

for username in usernames.index:
    p = subprocess.Popen(('git', 'log', '--oneline'), stdout=subprocess.PIPE, cwd=f'{direc}/{username}')
    commits = subprocess.check_output(('wc', '-l'), stdin=p.stdout).decode().strip()
    commits_rec.append(int(commits) - init_commits)
    p.wait()

    p = subprocess.Popen(('git', 'branch', '-l', '--remote'), stdout=subprocess.PIPE, cwd=f'{direc}/{username}')
    branches = subprocess.check_output(('wc', '-l'), stdin=p.stdout).decode().strip()
    branch_rec.append(int(branches) - 1)
    p.wait()

    diff = subprocess.Popen(('git', 'diff', rsa), stdout=subprocess.PIPE, cwd=f'{direc}/{username}')
    lines = subprocess.check_output(('wc', '-l'), stdin=diff.stdout).decode().strip()
    lines_rec.append(lines)
    diff.wait()

    diff = subprocess.Popen(('git', 'diff', rsa, filename), stdout=subprocess.PIPE, cwd=f'{direc}/{username}')
    pynb_lines = subprocess.check_output(('wc', '-l'), stdin=diff.stdout).decode().strip()
    pynb_lines_rec.append(pynb_lines)
    diff.wait()

    pynb_count = len(glob(f'{direc}/{username}/*.ipynb'))
    pynb_rec.append(pynb_count)

    py_count = len(glob(f'{direc}/{username}/*.py'))
    py_rec.append(py_count)


usernames['pynb files'] = pynb_rec
usernames['py files'] = py_rec
usernames['diff'] = lines_rec
usernames['pynb diff'] = pynb_lines_rec
usernames['commits'] = commits_rec
usernames['branches'] = branch_rec
usernames['grade'] = None

print(usernames)
