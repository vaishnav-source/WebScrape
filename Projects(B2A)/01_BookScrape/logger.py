import logging


logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO
)

logger = logging.getLogger(__name__)