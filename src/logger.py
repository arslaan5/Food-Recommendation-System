import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Define log directory
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)  # Ensure log directory exists

# Define log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__) 