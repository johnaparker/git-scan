#!/usr/bin/python3

import pandas as pd
from git import Repo
import subprocess
from glob import glob
import os
import libtmux

import argparse
from termcolor import colored

hw = 'hw5'
root = '/home/john/Documents/phys250/grading/'
db = pd.read_csv(f'{root}/db.csv', index_col=0)

print(db)

parser = argparse.ArgumentParser(prog='grade')
parser.add_argument('grade', nargs='?', type=float, help='total points', default=-1)

args = parser.parse_args()

if args.grade != -1:
    pwd = os.path.basename('./')
    username = os.path.basename(os.getcwd())

    db.loc[username, 'grade'] = args.grade
    db.to_csv(f'{root}/db.csv')

    # command = ['git', 'commit', '-am', 'feedback provided']
    # subprocess.call(command)
    # command = ['git', 'push']
    # subprocess.call(command)

server = libtmux.Server()

for username in db.index:
    grade = db.loc[username, 'grade']
    grading = db.loc[username, 'grading']

    if pd.isnull(grade) and grading == 'Yes':
        path = f'{root}/{hw}/{username}'
        # subprocess.call(f'gnome-terminal  --working-directory={path} -- "{root}/grade_tmux"', shell=True)

        session = server.find_where({ "session_name": "grading" })
        if session is None:
            session = server.new_session(session_name='grading', attach=False)
        server.switch_client('grading')

        w = session.new_window(window_name=username, start_directory=path)
        pane = w.attached_pane
        pane.send_keys('jupyter notebook', enter=True)

        pane = w.split_window(attach=True, start_directory=path)
        pane.resize_pane(height=100)
        pane.send_keys("export PATH=/home/john/Documents/phys250/grading:$PATH", enter=True)
        pane.send_keys("display", enter=True)
        pane.send_keys("tree", enter=True)
        pane.send_keys("git --no-pager branch -l --remote", enter=True)

        break
