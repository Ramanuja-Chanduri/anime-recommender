from src.dataloader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder

from config.config import config

from utils.logger import get_logger
from utils.custom_exceptions import CustomException

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build the pipeline...")

        loader = AnimeDataLoader(original_csv='data/anime_with_synopsis.csv', processed_csv='data/processed_anime.csv')
        processed_data_path = loader.load_and_process()

        logger.info("Data loaded and processed successfully.")

        vector_builder = VectorStoreBuilder(csv_path=processed_data_path, persist_directory=config.VECTOR_STORE_PATH)
        vector_builder.build_and_save_vector_store()

        logger.info("Vector store built successfully.")

        logger.info("Pipeline initialized successfully.")

    except Exception as e:
        logger.error(f"Error building pipeline: {str(e)}")
        raise CustomException("Failed to build pipeline", e)


if __name__ == "__main__":
    main()
