from aiohttp import web

from dnlp.handlers import deduplicate, detect, extract, tokenize


routes = [
    web.post('/detect', detect),
    web.post('/tokenize', toke