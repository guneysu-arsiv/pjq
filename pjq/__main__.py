#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

import sys
import json
import helpers


def main():
    global selectorstring, infile, obj
    if len(sys.argv) in [1, 4] or len(sys.argv) > 3:
        raise SystemExit(sys.argv[0] + " [infile selector]")
    elif len(sys.argv) == 2:
        infile = sys.stdin
        selectorstring = sys.argv[1]
    elif len(sys.argv) == 3:
        infile = open(sys.argv[1], 'rb')
        selectorstring = sys.argv[2]

    with infile:
        try:
            obj = json.load(infile)
        except ValueError, e:
            raise SystemExit(e)
    with sys.stdout:
        try:
            extracted = helpers.query(obj=obj, selector=selectorstring)

            json.dump(extracted, sys.stdout, sort_keys=False,
                      indent=4, separators=(',', ': '))
        except Exception, e:
            raise


if __name__ == '__main__':
    main()
