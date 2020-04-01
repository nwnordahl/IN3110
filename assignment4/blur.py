#!/usr/bin/env python3

import argparse
from blur_1 import blur_1
from blur_2 import blur_2
from blur_3 import blur_3

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blur images. \
If no flags are used, the numerical parts of the code \
will use regular Python.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--vectorized", action="store_true",
                       help="vectorized implementation of the blur algorithm")
    group.add_argument("-n", "--numba", action="store_true",
                       help="numba enhanced implementation \
of the blur algorithm")
    parser.add_argument("infile", help="filename of image you want to blur")
    parser.add_argument("outfile", help="save blurred image as outfile")
    args = parser.parse_args()

    if args.vectorized:
        blur_2(args.infile, args.outfile)
    elif args.numba:
        blur_3(args.infile, args.outfile)
    else:
        blur_1(args.infile, args.outfile)
