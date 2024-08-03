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
        "-o",
        "--outputfile",
        action="store",
        help="Write machine output results to the output file. Does not write normal output",
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

    if args.outputfile:
        outfile = open(args.outputfile, "w+", encoding="utf-8")

    with open(input_filename, encoding="utf-8") as fp:
        if args.verbose:
            print(f"Looking for cards in file {input_filename}")
        linenum = 0
        for line in fp:
            linenum += 1
            (card_found, card_type, found_pattern) = ccregex.find_cards(
                args, line.strip(), linenum, input_filename
            )
            if card_found:
                cardcount += 1
                ccregex.found_card(
                    args,
                    line.strip(),
                    card_type,
                    found_pattern,
                    linenum,
                    input_filename,
                )
            if card_found and args.machine:
                valid_card_number = ccregex.validate_cardnumber(
                    args, found_pattern.group(0)
                )

                if args.outputfile:
                    outfile.write(
                        f"{linenum},{input_filename},{found_pattern.group(0)},{valid_card_number}\n"
                    )
                else:
                    print(
                        f"{linenum},{input_filename},{found_pattern.group(0)},{valid_card_number}"
                    )
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

    if args.outputfile:
        outfile.close()

