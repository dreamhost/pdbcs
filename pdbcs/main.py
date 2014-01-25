#!/usr/bin/env python

import argparse
import os
import pdb
import sys

import pkg_resources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('script')
    args, scriptargs = parser.parse_known_args()

    script_name = os.path.basename(args.script)
    ep = pkg_resources.iter_entry_points('console_scripts', script_name).next()
    f = ep.load()

    sys.argv = [args.script]
    sys.argv.extend(scriptargs)
    pdb.runcall(f)

if __name__ == '__main__':
    sys.exit(main())
