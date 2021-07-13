
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
from dnlp.postprocess import remap_prediction
from dnlp.preprocess import fix_bad_unicode, normalize_html, normalize_whitespace, preprocess_text


# fastText
MODEL_PATH = os.environ.get('MODEL_PATH', None)
if not MODEL_PATH:
    raise RuntimeError('Environment variable "MODEL_PATH" empty')
FT_MODEL = ft_load_model(MODEL_PATH)

# nltk punkt
SENT_TOKENIZER = {}

# trafilatura config
TRAFILATURA_CONFIG = use_config()
TRAFILATURA_CONFIG.set('DEFAULT', 'EXTRACTION_TIMEOUT', '0')


async def tokenize(request):
    post_data = await request.post()
    param_text = post_data.get('text', '')

    param_text = fix_bad_unicode(param_text, normalization='NFC')
    param_text = normalize_whitespace(param_text)
    param_text = param_text.strip()

    if not param_text:
        return abort('empty "text" parameter')

    param_lang = post_data.get('lang', 'en')

    if param_lang in PUNKT_LANGUAGES.keys():
        if param_lang not in SENT_TOKENIZER.keys():
            # first tokenizer load (may be slow)