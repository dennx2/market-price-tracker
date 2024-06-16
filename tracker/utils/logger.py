import logging
import os
from datetime import datetime

def setup_logger() -> logging.Logger:
    # Set up the root logger with the desired configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Create a module-level logger
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        log_base_directory = "logs"

        # Get current year and month
        current_date = datetime.now()
        year = current_date.strftime("%Y")
        month = current_date.strftime("%m")

        # Create directory structure by year and month
        log_directory = os.path.join(log_base_directory, year, month)
        os.makedirs(log_directory, exist_ok=True)

        # Create handlers for different log levels
        # Define file paths for each log level
        info_handler = logging.FileHandler(os.path.join(log_directory, "info.log"))
        info_handler.setLevel(logging.INFO)

        error_handler = logging.FileHandler(os.path.join(log_directory, "error.log"))
        error_handler.setLevel(logging.ERROR)

        # Define formatters for the handlers
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        info_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(info_handler)
        logger.addHandler(error_handler)

    return logger


# Usage:
# logger = setup_logger()
