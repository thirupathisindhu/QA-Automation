import logging

logging.basicConfig(
    filename="execution.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger()
