import logging
from pathlib import Path
from datetime import datetime

from ETL.extract import extract_products, extract_users
from ETL.transform import transform_product, transform_users
from ETL.load import load_data, verify_data


# Define project directories.
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"


# Configure logging.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger(__name__)


def run_pipeline():
    """Execute the complete ETL pipeline."""

    start_time = datetime.now()

    logger.info("=" * 60)
    logger.info("Fake Store ETL pipeline started")
    logger.info("=" * 60)

    try:
        # STEP 1: EXTRACT
        logger.info("STEP 1: Extracting data")

        product_df = extract_products()
        user_df = extract_users()

        # STEP 2: TRANSFORM
        logger.info("STEP 2: Transforming data")

        transformed_products = transform_product(product_df)
        transformed_users = transform_users(user_df)

        # STEP 3: LOAD
        logger.info("STEP 3: Loading data into SQLite")

        load_data(
            transformed_products,
            transformed_users
        )

        # STEP 4: VERIFY
        logger.info("STEP 4: Verifying database records")

        verify_data()

        # Calculate execution duration.
        duration = (datetime.now() - start_time).total_seconds()

        logger.info("=" * 60)
        logger.info("ETL PIPELINE COMPLETED SUCCESSFULLY")
        logger.info(
            "Products processed: %d",
            len(transformed_products)
        )
        logger.info(
            "Users processed: %d",
            len(transformed_users)
        )
        logger.info("Execution time: %.2f seconds", duration)
        logger.info("=" * 60)

    except Exception:
        logger.exception("ETL PIPELINE FAILED")
        raise


if __name__ == "__main__":
    run_pipeline()