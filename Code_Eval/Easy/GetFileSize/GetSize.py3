#!/usr/bin/env python

import os
from sys import argv

in_file = argv[1]

def get_size(filename):
    st = os.stat(filename)
    print(st.st_size)

if __name__ == '__main__':
     get_size(in_file)
