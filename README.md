# ccfind - Credit Card Hunter

This code is designed to scrape through text / log / config files - searching for number patterns that
match credit card numbers. 

It then attempts to identify the card number, and do some simple validation to check if the number sequences pass the simple CCard validation checks.

## Usage
- *ccfind.py* **-h** provides help
- *ccfind.py* **-a** Enables a very simplistic pattern search, possible false positives (Default: off)
- *ccfind.py* **-m** provides CSV formatted output - that can then be processed by other systems.
- *ccfind.py* **-o filename** writes **-m** output to specified filename
- *ccfind.py* **-d** and **-v** turn on additional messaging to show the details of whats been discovered along the way.
- *ccfind.py* **-c** adds color


## Example options

$ ./ccfind.py -s -o output.csv -m inputfile.log


