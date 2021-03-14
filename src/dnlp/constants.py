import re
import sys
import unicodedata


PUNCT_TRANSLATE_UNICODE = dict.fromkeys(
    (i for i in range(sys.maxunicode)
     if unicodedata.category(chr(i)).startswith('P')),
    u' ')

LINEBREAK_REGEX = re.compile(r