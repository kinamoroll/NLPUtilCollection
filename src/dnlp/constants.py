import re
import sys
import unicodedata


PUNCT_TRANSLATE_UNICODE = dict.fromkeys(
    (i for i in range(sys.maxunicode)
     if unicodedata.category(chr(i)).startswith('P')),
    u' ')

LINEBREAK_REGEX = re.compile(r'((\r\n)|[\n\v])+')

NONBREAKING_SPACE_REGEX = re.compile(r'(?!\n)\s+')

EMAIL_REGEX = re.compile(
    r"(