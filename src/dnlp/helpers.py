import asyncio
from functools import wraps
from typing import List

from Levenshtein import ratio as levenshtein_ratio
from aiohttp.web import json_response


def sync(fu