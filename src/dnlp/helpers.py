import asyncio
from functools import wraps
from typing import List

from Levenshtein import ratio as levenshtein_ratio
from aiohttp.web import json_response


def sync(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.get_event_loop().run_until_complete(func(*args, **kwargs))
    return wrapper


def abort(error_text: str):
    return json_response(
        {
            'error': error_text,
        },
        status=400,
    )


def deduplicate_sen