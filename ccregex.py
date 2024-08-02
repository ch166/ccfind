import re
import sys

import utils
import tty_colors


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
        print(f"{tty_colors.BLUE}", end="")
    print(f"file:{input_filename}: ", end="")
    if args.color:
        print(f"{tty_colors.GREEN}", end="")
    print(f"line:{linenum} Potential {cardType} card found: Valid: {valid_card_number}")
    if args.pattern:
        if args.color:
            print(f"{tty_colors.RED}", end="")
        if args.verbose:
            print(f"Regex Match:", end="")
        print(f"{found_match.group(0)}")
    if args.context:
        if args.color:
            print(f"{tty_colors.RED}", end="")
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
