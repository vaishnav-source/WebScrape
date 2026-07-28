import logging
import os

from config import LOG_FILE, LOG_LEVEL


log_directory = os.path.dirname(LOG_FILE)

if log_directory:
    os.makedirs(log_directory, exist_ok=True)


logging.basicConfig(
    filename=LOG_FILE,
    level=getattr(logging, LOG_LEVEL),
)

logger = logging.getLogger(__name__)