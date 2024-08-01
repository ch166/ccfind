#!/usr/bin/env python3

import re
import sys

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


def foundCard(input_line, cardType, linenum):
    """Report card discovery information"""
    print(f"{BLUE}[!]{GREEN}{linenum} Potential {cardType} card found")
    print(f"{RED}Regex Match: {input_line}")


def findCards(input_line, linenum):
    """Regex search through line"""
    if (
        re.match(
            r'\b(?:3[47]\d{2}([\ \-]?)\d{6}\1\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([\ \-]?)\d{4}\2\d{4}\2)\d{4}\b',
            input_line,
        )
        is not None
    ):
        card_type = "Visa/MasterCard/American Express/Discover"
        foundCard(input_line, card_type)
    elif (
        re.match(
            r'(?:3[47]\d{2}([ \-]?)\d{6}\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([ \-]?)\d{4}\d{4})\d{4}',
            input_line,
        )
        is not None
    ):
        card_type = "credit/debit"
        foundCard(input_line, card_type)
    elif (
        re.match(
            r"(?ms)(.*)\b(?:4[0-9]{8}(?:[0-9]{3})?|5[1-5][0-9]{10}|6(?:011|5[0-9]{2})[0-9]{8}|3[47][0-9]{9}|3(?:0[0-5]|[68][0-9])[0-9]{7}|(?:2131|1800|35\d{3})\d{7})(\d{4}\b.*)",
            input_line,
        )
        is not None
    ):
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b3[47][0-9]{13}\b.", input_line) is not None:
        card_type = "American Express (AMEX)"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b(6541|6556)[0-9]{12}\b.", input_line) is not None:
        card_type = "BCGlobal"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b389[0-9]{11}\b.", input_line) is not None:
        card_type = "Carte Blanche"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b3(?:0[0-5]|[68][0-9])[0-9]{11}\b.", input_line) is not None:
        card_type = "Diners"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b6(?:011|5[0-9]{2})[0-9]{12}\b.", input_line) is not None:
        card_type = "Discover"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b63[7-9][0-9]{13}\b.", input_line) is not None:
        card_type = "Insta Paymentcard"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b(?:2131|1800|35\d{3})\d{11}\b.", input_line) is not None:
        card_type = "JCB"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b9[0-9]{15}\b.", input_line) is not None:
        card_type = "Korean Local card"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b(6304|6706|6709|6771)[0-9]{12,15}\b.", input_line) is not None:
        card_type = "LaserCard"
        foundCard(input_line, card_type, linenum)
    elif (
        re.match(r"\b(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}\b.", input_line)
        is not None
    ):
        card_type = "Maestro"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b5[1-5][0-9]{14}\b.", input_line) is not None:
        card_type = "Mastercard"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"5[1-5][0-9]{14}", input_line) is not None:
        card_type = "SoloCard"
        foundCard(input_line, card_type, linenum)
    elif (
        re.match(
            r"\b(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}\b.", input_line
        )
        is not None
    ):
        card_type = "SwitchCard"
        foundCard(input_line, card_type, linenum)
    elif (
        re.match(
            r"\b(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}\b.",
            input_line,
        )
        is not None
    ):
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b4[0-9]{12}(?:[0-9]{3})?\b.", input_line) is not None:
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)
    elif (
        re.match(
            r"\b(?:3[47]\d{2}([ \-]?)\d{6}\b\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([ \-]?)\d{4}\b\d{4}\b)\d{4}\b",
            input_line,
        )
        is not None
    ):
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)
    elif (
        re.match(
            r"(?:3[47]\d{2}([ \-]?)\d{6}\b\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([ \-]?)\d{4}\b\d{4}\b)\d{4}",
            input_line,
        )
        is not None
    ):
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b(62[0-9]{14,17})\b.", input_line) is not None:
        card_type = "ICARD"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b(4[0-9]{14,17})\b.", input_line) is not None:
        card_type = "Visa Mastercard"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"(4[0-9]{14,17})", input_line) is not None:
        card_type = "Visa Mastercard"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"((?<!\.)4[0-9]{14,17})", input_line) is not None:
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\b.", input_line) is not None:
        card_type = "Visa Mastercard"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", input_line) is not None:
        card_type = "Visa"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"(0200[0-9]{43})(4[0-9]{12}[0-9]{3})", input_line) is not None:
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)
    elif re.match(r"^4\d{3}([ \-]?)\d{4}\d{4}\d{4}$", input_line) is not None:
        card_type = "credit/debit"
        foundCard(input_line, card_type, linenum)


if __name__ == "__main__":
    with open(sys.argv[1]) as fp:
        print("Looking for cards...")
        linenum = 0
        for line in fp:
            linenum += 1
            findCards(line.strip(), linenum)
        sys.stdout.write(RESET)
    print("Done!")
