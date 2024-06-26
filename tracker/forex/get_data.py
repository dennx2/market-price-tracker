from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from ..utils.logger import setup_logger

logger = setup_logger()


def google_exchange_rate(currency_pair: str) -> float | None:
    """
    Get currency exchange rate through google search
    """

    # Setup the webdriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headless Chrome
    options.add_argument("--incognito")  # Run in incognito mode
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Wait for the search box to be visible
        time.sleep(2)

        # Find the search box element
        search_box = driver.find_element(By.NAME, "q")

        # Enter a search query
        search_box.send_keys(currency_pair)

        # Press Enter to initiate the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(2)

        # Find the element with the class "b1hJbf" and get the data-exchange-rate attribute
        element = driver.find_element(By.CLASS_NAME, "b1hJbf")
        exchange_rate = element.get_attribute("data-exchange-rate")

        # Print the exchange rate
        if exchange_rate:
            logger.info(f"The exchange rate is: {exchange_rate}")
            exchange_rate = float(exchange_rate)
            return exchange_rate
        else:
            logger.warning("Exchange rate attribute not found in the element")
            return None

    except Exception as e:
        logger.error("An error occurred in google_exchange_rate", exc_info=True)
        return None

    finally:
        # Close the driver
        driver.quit()
