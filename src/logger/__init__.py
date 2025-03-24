import logging
import os
from logging.handlers import RotatingFileHandler  # For log rotation
from from_root import from_root  # Utility to get the root directory of the project
from datetime import datetime  # For timestamping log files

# Constants for log configuration
LOG_DIR = 'logs'  # Directory to store log files
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Log file name with timestamp
MAX_LOG_SIZE = 5 * 1024 * 1024  # Maximum log file size (5 MB)
BACKUP_COUNT = 3  # Number of backup log files to keep

# Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR)  # Full path to the log directory
os.makedirs(log_dir_path, exist_ok=True)  # Create log directory if it doesn't exist
log_file_path = os.path.join(log_dir_path, LOG_FILE)  # Full path to the log file

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    Logs are written to both a file and the console.
    """
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the base logging level to DEBUG

    # Define formatter for log messages
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file_path, 
        maxBytes=MAX_LOG_SIZE,  # Rotate log file when it reaches max size
        backupCount=BACKUP_COUNT  # Keep up to 3 backup log files
    )
    file_handler.setFormatter(formatter)  # Apply the formatter
    file_handler.setLevel(logging.DEBUG)  # Log all levels (DEBUG and above) to file

    # Console handler for output to the terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)  # Apply the formatter
    console_handler.setLevel(logging.INFO)  # Log INFO level and above to console

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()