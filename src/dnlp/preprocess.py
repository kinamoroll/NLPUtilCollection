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
    URL_REGE