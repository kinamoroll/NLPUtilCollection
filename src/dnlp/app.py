
import asyncio
import logging

from aiohttp import web

from dnlp.helpers import sync
from dnlp.routes import routes


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
)
logger = logging.getLogger(__name__)
