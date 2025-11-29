import logging
import os
from datetime import datetime

def get_logger(name: str = None):
    """
    Creates and returns a logger instance.
    Logs both to console and to a rotating file.
    """

    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    # Log file name with timestamp
    log_filename = datetime.now().strftime("logs/test_run_%Y-%m-%d_%H-%M-%S.log")

    # Create logger
    logger = logging.getLogger(name if name else "framework")
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # --- Console Handler ---
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)

    # --- File Handler ---
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
