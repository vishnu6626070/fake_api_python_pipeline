import logging
import sqlite3
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "fake_store.db"


def load_data(product_df, user_df):
    """Load products and users into the SQLite database."""

    logger.info("Starting data loading")

    # Create the data directory if it does not exist.
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with sqlite3.connect(DB_PATH, timeout=30) as connection:

            # Load both DataFrames within the same transaction.
            product_df.to_sql(
                name="products",
                con=connection,
                if_exists="replace",
                index=False
            )

            logger.info(
                "Loaded %d products into SQLite",
                len(product_df)
            )

            user_df.to_sql(
                name="users",
                con=connection,
                if_exists="replace",
                index=False
            )

            logger.info(
                "Loaded %d users into SQLite",
                len(user_df)
            )

        logger.info("Data loading completed successfully")
        logger.info("Database location: %s", DB_PATH)

    except (sqlite3.Error, ValueError, TypeError):
        logger.exception("Data loading failed")
        raise


def verify_data():
    """Verify the number of records in each database table."""

    logger.info("Starting database verification")

    try:
        with sqlite3.connect(DB_PATH, timeout=30) as connection:

            cursor = connection.cursor()

            tables = ["products", "users"]

            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]

                logger.info(
                    "Verification successful: %s contains %d records",
                    table,
                    count
                )

    except sqlite3.Error:
        logger.exception("Database verification failed")
        raise