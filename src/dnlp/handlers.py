
import asyncio
import os

from aiohttp.web import json_response
from aiohttp.web_response import Response
from fasttext import load_model as ft_load_model
from nltk.data import load as nltk_load
from trafilatura.core import extract as trafilatura_extract
from trafilatura.settings import use_config

from dnlp.helpers import abort, deduplicate_sentences
from dnlp.languages import PUNKT_LANGUAGES