import re
from typing import Optional

from ftfy import fix_text

from dnlp.constants import (
    EMAIL_REGEX,
    LINEBREAK_REGEX,
    NONBREAKING_SPACE_REGEX,
    NUMBERS_REGEX,
    PUNCT_TRANSLATE_UNICODE,
    SHORT_URL_REGEX,
    URL_REGEX,
)


def preprocess_text(text: str) -> str:
    """Based on `textacy.preprocess_text` method"""
    # small speedup
    text = text.strip()
    if not text:
        return text

    text = fix_bad_unicode(text, normalization='NFC')

    # custom `replace_with` values for more detectable results
    text = replace_urls(text, replace_with=' ')
    text = replace_emails(text, replace_with=' ')
    text = replace_numbers(text, replace_with=' ')

    text = remove_punct(text)
    text = text.lower()
    text = normalize_whitespace(text)

    # fastText work only with 1 line of text
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')

    return text.strip()


def fix_bad_unicode(text: str, normalization: str = 'NFC') -> str:
    """
