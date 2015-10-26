#!/usr/bin/env python

import sys

def check_endian():
    system_type = sys.byteorder
    if system_type == 'little':
        print('LittleEndian')
    elif system_type == 'big':
        print('BigEndian')
    else:
        sys.exit('Unable to determine')


if __name__ == '__main__':
    check_endian()