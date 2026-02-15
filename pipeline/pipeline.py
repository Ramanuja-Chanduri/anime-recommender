from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import config

from utils.logger import get_logger
from utils.custom_exceptions import CustomException

logger = get_logger(__name__)


class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline...")

            vector_build = VectorStoreBuilder(csv_path="", persist_directory=persist_dir)
            retriever = vector_build.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=config.GROQ_API_KEY, model_name=config.MODEL_NAME)

            logger.info("Pipeline initialized successfully.")

        except Exception as e:
            logger.error(f"Error initializing pipeline: {str(e)}")
            raise CustomException("Failed to initialize pipeline", e)
        
    def recommend(self, user_query: str):
        try:
            logger.info(f"Received user query: {user_query}")

            recommendation = self.recommender.get_recommendation(user_query)

            logger.info("Recommendation generated successfully.")
            return recommendation
        except Exception as e:
            logger.error(f"Error generating recommendation: {str(e)}")
            raise CustomException("Failed to generate recommendation", e)

