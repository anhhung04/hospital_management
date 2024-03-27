import structlog
from config import config
processors=[
    structlog.processors.add_log_level,
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.processors.dict_tracebacks,
]

if config["PROD"]:
    processors.append(structlog.processors.JSONRenderer())
else:
    processors.append(structlog.dev.ConsoleRenderer())

structlog.configure(
    processors=processors,
)

logger = structlog.get_logger()

__all__ = ["logger"]
