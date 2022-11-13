#!/usr/bin/python

import subprocess, sys

commands = [
    ['lualatex', sys.argv[1] + '.tex'],
    ['bibtex', sys.argv[1] + '.aux'],
    ['lualatex', sys.argv[1] + '.tex'],
    ['lualatex', sys.argv[1] + '.tex']
]

for c in commands:
    subprocess.call(c)
