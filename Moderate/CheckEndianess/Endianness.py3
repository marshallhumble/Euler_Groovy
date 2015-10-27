#!/usr/bin/env python

from sys import byteorder


def check_endian():
    print({'big': 'BigEndian', 'little': 'LittleEndian'}.get(byteorder))


if __name__ == '__main__':
    check_endian()