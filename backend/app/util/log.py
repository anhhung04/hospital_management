import json
import logging
import time
from logging import Formatter


class JsonFormatter(Formatter):
    def __init__(self):
        super(JsonFormatter, self).__init__()

    def format(self, record):
        json_record = {}
        json_record["timestamp"] = time.time()
        json_record["level"] = record.levelname
        json_record["message"] = record.getMessage()
        return json.dumps(json_record)


logger = logging.root
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.handlers = [handler]
logger.setLevel(logging.INFO)
