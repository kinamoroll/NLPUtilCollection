import re
import sys
import unicodedata


PUNCT_TRANSLATE_UNICODE = dict.fromkeys(
    (i for i in range(sys.maxu