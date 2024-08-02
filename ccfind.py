#!/usr/bin/env python3

import re
import sys
import argparse

import utils

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


def found_card(args, input_line, cardType, found_match, linenum, input_filename):
    """Report card discovery information"""
    valid_card_number = utils.validate_credit_card(found_match.group(0))
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


def find_cards(args, input_line, linenum, input_filename):
    """Regex search through line"""
    found_pattern = None
    found_pattern = re.search(
        r"\b(?:3[47]\d{2}([\ \-]?)\d{6}\1\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([\ \-]?)\d{4}\2\d{4}\2)\d{4}\b",
        input_line,
    )
    if found_pattern is not None:
        card_type = "Visa/MasterCard/American Express/Discover"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(
        r"(?:3[47]\d{2}([ \-]?)\d{6}\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([ \-]?)\d{4}\d{4})\d{4}",
        input_line,
    )
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(
        r"(?ms)(.*)\b(?:4[0-9]{8}(?:[0-9]{3})?|5[1-5][0-9]{10}|6(?:011|5[0-9]{2})[0-9]{8}|3[47][0-9]{9}|3(?:0[0-5]|[68][0-9])[0-9]{7}|(?:2131|1800|35\d{3})\d{7})(\d{4}\b.*)",
        input_line,
    )
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b3[47][0-9]{13}\b.", input_line)
    if found_pattern is not None:
        card_type = "American Express (AMEX)"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b(6541|6556)[0-9]{12}\b.", input_line)
    if found_pattern is not None:
        card_type = "BCGlobal"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b389[0-9]{11}\b.", input_line)
    if found_pattern is not None:
        card_type = "Carte Blanche"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b3(?:0[0-5]|[68][0-9])[0-9]{11}\b.", input_line)
    if found_pattern is not None:
        card_type = "Diners"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b6(?:011|5[0-9]{2})[0-9]{12}\b.", input_line)
    if found_pattern is not None:
        card_type = "Discover"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b63[7-9][0-9]{13}\b.", input_line)
    if found_pattern is not None:
        card_type = "Insta Paymentcard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b(?:2131|1800|35\d{3})\d{11}\b.", input_line)
    if found_pattern is not None:
        card_type = "JCB"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b9[0-9]{15}\b.", input_line)
    if found_pattern is not None:
        card_type = "Korean Local card"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b(6304|6706|6709|6771)[0-9]{12,15}\b.", input_line)
    if found_pattern is not None:
        card_type = "LaserCard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(
        r"\b(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}\b.", input_line
    )
    if found_pattern is not None:
        card_type = "Maestro"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b5[1-5][0-9]{14}\b.", input_line)
    if found_pattern is not None:
        card_type = "Mastercard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"5[1-5][0-9]{14}", input_line)
    if found_pattern is not None:
        card_type = "SoloCard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1

    found_pattern = re.search(
        r"\b(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}\b.",
        input_line,
    )
    if found_pattern is not None:
        card_type = "SwitchCard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(
        r"\b(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}\b.",
        input_line,
    )
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b4[0-9]{12}(?:[0-9]{3})?\b.", input_line)
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(
        r"\b(?:3[47]\d{2}([ \-]?)\d{6}\b\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([ \-]?)\d{4}\b\d{4}\b)\d{4}\b",
        input_line,
    )
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(
        r"(?:3[47]\d{2}([ \-]?)\d{6}\b\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([ \-]?)\d{4}\b\d{4}\b)\d{4}",
        input_line,
    )
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b(62[0-9]{14,17})\b.", input_line)
    if found_pattern is not None:
        card_type = "ICARD"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"\b(4[0-9]{14,17})\b.", input_line)
    if found_pattern is not None:
        card_type = "Visa Mastercard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"(4[0-9]{14,17})", input_line)
    if found_pattern is not None:
        card_type = "Visa Mastercard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"((?<!\.)4[0-9]{14,17})", input_line)
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(
        r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\b.", input_line
    )
    if found_pattern is not None:
        card_type = "Visa Mastercard"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"^4[0-9]{12}(?:[0-9]{3})?$", input_line)
    if found_pattern is not None:
        card_type = "Visa"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"(0200[0-9]{43})(4[0-9]{12}[0-9]{3})", input_line)
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    found_pattern = re.search(r"^4\d{3}([ \-]?)\d{4}\d{4}\d{4}$", input_line)
    if found_pattern is not None:
        card_type = "credit/debit"
        found_card(args, input_line, card_type, found_pattern, linenum, input_filename)
        return 1
    return 0


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
            cardcount += find_cards(args, line.strip(), linenum, input_filename)
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
