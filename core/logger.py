from loguru import logger
from pathlib import Path

LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)

logger.add(
    LOG_DIR / "application.log",
    rotation="5 MB",
    retention="30 days",
    level="DEBUG"
)
