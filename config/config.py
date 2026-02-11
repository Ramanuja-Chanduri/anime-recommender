import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class to manage all environment variables and settings."""
    
    def __init__(self):
        # API Keys
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        self.HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
        
        # Model Configuration
        self.MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")
        self.EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")
        
        # Validate required environment variables
        self._validate()
    
    def _validate(self):
        """Validate that all required environment variables are set."""
        required_vars = {
            "GROQ_API_KEY": self.GROQ_API_KEY,
            "HUGGINGFACE_API_TOKEN": self.HUGGINGFACE_API_TOKEN,
        }
        
        missing_vars = [var for var, value in required_vars.items() if not value]
        
        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )
    
    def __repr__(self):
        return f"Config(MODEL_NAME={self.MODEL_NAME})"


# Create a singleton instance
config = Config()