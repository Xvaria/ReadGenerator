#!/usr/bin/python3
''''''
import os
import re
import requests
import datetime


git = os.popen('git remote show origin').read().split(" ")[6][:-1]
repo = os.popen('pwd').read().split("/")[-1][:-1]
files = os.popen('ls').read().split("\n")[:-1]
files.remove("README.md")
web = str(datetime.datetime.now()).split(" ")[0]
print(web)
print(repo)
print(files)
