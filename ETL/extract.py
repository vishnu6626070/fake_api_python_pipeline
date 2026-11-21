import logging

import pandas as pd
import requests

BASE_URL = "https://fakestoreapi.com"
TIMEOUT = 30

logger = logging.getLogger(__name__)


def extract_products():
    """Extract product data from the Fake Store API."""

    url = f"{BASE_URL}/products"

    logger.info("Starting product extraction")

    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()
        product_df = pd.DataFrame(data)

        if not isinstance(data, list):
            raise ValueError("Expected a list of products from the API")

        logger.info(
            "Product extraction successful: %d records",
            len(product_df)
        )

        return product_df

    except (requests.RequestException, ValueError) as error:
        logger.exception("Product extraction failed: %s", error)
        raise


def extract_users():
    """Extract user data from the Fake Store API."""

    url = f"{BASE_URL}/users"

    logger.info("Starting user extraction")

    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Expected a list of users from the API")

        user_df = pd.DataFrame(data)

        logger.info(
            "User extraction successful: %d records",
            len(user_df)
        )

        return user_df

    except (requests.RequestException, ValueError) as error:
        logger.exception("User extraction failed: %s", error)
        raise