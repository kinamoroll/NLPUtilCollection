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

    text = fix_bad_unicode(text, normal