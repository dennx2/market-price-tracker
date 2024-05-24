from dotenv import load_dotenv
import os
import requests
from .logger import setup_logger

# Load the .env file
load_dotenv()

# Access the variables
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

TELEGRAM_BASE_URL = "https://api.telegram.org/bot"

logger = setup_logger()


def send_notification(chat_id: str, message: str) -> None:
    """Function to send a notification to Telegram"""

    # Telegram API endpoint for sending messages
    telegram_api_url = f"{TELEGRAM_BASE_URL}{bot_token}/sendMessage"

    # Set up the message parameters
    params = {"chat_id": chat_id, "text": message}

    # Send the message using the requests library
    response = requests.post(telegram_api_url, params=params)

    # Check the response status
    if response.status_code == 200:
        logger.info("Telegram notification sent successfully.")
    else:
        logger.error(
            f"Failed to send Telegram notification. Status code: {response.status_code}"
        )

    return None
