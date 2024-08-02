#!/usr/bin/env python3

import re
import sys
import argparse

import utils
import ccregex

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


def found_card(args, input_line, cardType, found_match, linenum, input_filename):
    """Report card discovery information"""
    card_string = found_match.group(0)
    card_number = utils.prune_chars_from_int(card_string)
    if args.debug:
        print(f"{card_string}:{card_number}")
    valid_card_number = utils.validate_credit_card(card_number)
    if args.machine:
        print(f"{linenum},{input_filename},{found_match.group(0)},{valid_card_number}")
        return
    if args.color:
        print(f"{BLUE}", end="")
    print(f"file:{input_filename}: ", end="")
    if args.color:
        print(f"{GREEN}", end="")
    print(f"line:{linenum} Potential {cardType} card found: Valid: {valid_card_number}")
    if args.pattern:
        if args.color:
            print(f"{RED}", end="")
        if args.verbose:
            print(f"Regex Match:", end="")
        print(f"{found_match.group(0)}")
    if args.context:
        if args.color:
            print(f"{RED}", end="")
        if args.verbose:
            print(f"Regex Match:", end="")
        print(f"{found_match.string}")


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
            print(f"{RESET}", end="")
    if args.summary:
        if args.color:
            print(f"{CYAN}", end="")
        print(f"Summary: file:{input_filename}: matches:{cardcount}")
