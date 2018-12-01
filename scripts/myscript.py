#!/usr/bin/python

import os
import sys


parent_dir = os.path.split(os.path.dirname(__file__))[-1]
if dir == 'scripts':
    sys.path.append(os.path.join(parent_dir, '..'))

from project import MyClass


def main():
    c = MyClass()
    print(c.message)


if __name__ == "__main__":
    main()