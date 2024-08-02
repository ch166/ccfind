#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
"""Collection of functions to search for CCard/Debit card numbers in a file"""

import argparse

import ccregex
import tty_colors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ccfind",
        description="Searches text files for patterns matching credit cards",
    )
    parser.add_argument(
        "filename", help="file to be searched for patterns matching credit cards"
    )
    parser.add_argument(
        "-c",
        "--color",
        action="store_true",
        help="Display colors in output (Default: off)",
    )
    parser.add_argument(
        "-t",
        "--testfile",
        action="store",
        help="File containing pattern of known test credit cards (optional)",
    )
    parser.add_argument(
        "-s",
        "--summary",
        action="store_true",
        help="Print summary line at end of output",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        action="store_true",
        help="Print exact regex match on separate line",
    )
    parser.add_argument(
        "-x",
        "--context",
        action="store_true",
        help="Print regex match inside content on separate line",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Print debugging progress details"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print additional progress details"
    )
    parser.add_argument(
        "-m", "--machine", action="store_true", help="Machine Processable Output"
    )

    args = parser.parse_args()
    input_filename = args.filename
    cardcount = 0
    with open(input_filename) as fp:
        if args.verbose:
            print(f"Looking for cards in file {input_filename}")
        linenum = 0
        for line in fp:
            linenum += 1
            cardcount += ccregex.find_cards(args, line.strip(), linenum, input_filename)
            if args.debug:
                if linenum % 2 == 0:
                    print(".", end="", flush=True)
                else:
                    print("-", end="", flush=True)
        if args.color:
            print(f"{tty_colors.RESET}", end="")
    if args.summary:
        if args.color:
            print(f"{tty_colors.CYAN}", end="")
        print(f"Summary: file:{input_filename}: matches:{cardcount}")
