#!/usr/bin/env python3

from __future__ import print_function

import argparse
import sys

def main():
    ''' Parse command line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--org', type=str,
                        help='Clone the repos of this organisation')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show verbose information.')

    args, otherthings = parser.parse_known_args()
    argc = len(otherthings)

    verbosity = None
    if args.verbose:
        verbosity = 1

    pass


if __name__ == '__main__':
    sys.exit(main())
