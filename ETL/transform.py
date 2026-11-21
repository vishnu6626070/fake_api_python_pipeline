import logging

import pandas as pd

logger = logging.getLogger(__name__)


def transform_product(product_df):
    """Clean and transform the product DataFrame."""

    logger.info("Starting product transformation")

    if product_df.empty:
        raise ValueError("Product DataFrame is empty")

    df = product_df.copy()

    df = df.rename(
        columns={
            "id": "product_id",
            "title": "product_name",
            "price": "product_price",
            "description": "product_description",
            "category": "product_category"
        }
    )

    required_columns = [
        "product_id",
        "product_name",
        "product_price",
        "product_category",
        "product_description"
    ]

    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing product columns: {sorted(missing_columns)}"
        )

    df = df[required_columns].copy()

    df["product_price"] = pd.to_numeric(
        df["product_price"],
        errors="raise"
    )

    if df["product_id"].isna().any():
        raise ValueError("Product IDs cannot be missing")

    if df["product_id"].duplicated().any():
        raise ValueError("Duplicate product IDs found")

    logger.info(
        "Product transformation successful: %d records",
        len(df)
    )

    return df


def transform_users(user_df):
    """Clean and transform the user DataFrame."""

    logger.info("Starting user transformation")

    if user_df.empty:
        raise ValueError("User DataFrame is empty")

    df = user_df.copy()

    required_columns = [
        "id",
        "email",
        "username",
        "name",
        "address"
    ]

    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing user columns: {sorted(missing_columns)}"
        )

    # Extract nested name fields.
    df["first_name"] = df["name"].apply(
        lambda x: x.get("firstname") if isinstance(x, dict) else None
    )

    df["last_name"] = df["name"].apply(
        lambda x: x.get("lastname") if isinstance(x, dict) else None
    )

    # Extract nested address fields.
    df["street"] = df["address"].apply(
        lambda x: x.get("street") if isinstance(x, dict) else None
    )

    df["city"] = df["address"].apply(
        lambda x: x.get("city") if isinstance(x, dict) else None
    )

    df["zipcode"] = df["address"].apply(
        lambda x: x.get("zipcode") if isinstance(x, dict) else None
    )

    # Rename columns.
    df = df.rename(
        columns={
            "id": "user_id",
            "email": "user_email"
        }
    )

    # Select the required columns.
    df = df[
        [
            "user_id",
            "user_email",
            "username",
            "first_name",
            "last_name",
            "street",
            "city",
            "zipcode"
        ]
    ].copy()

    if df["user_id"].isna().any():
        raise ValueError("User IDs cannot be missing")

    if df["user_id"].duplicated().any():
        raise ValueError("Duplicate user IDs found")

    logger.info(
        "User transformation successful: %d records",
        len(df)
    )

    return df