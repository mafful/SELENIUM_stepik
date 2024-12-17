import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers for console and file output
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('test_log.log')  # Logs will be saved in 'test_log.log'

# Set logging levels for handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)