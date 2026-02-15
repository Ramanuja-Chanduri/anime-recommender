# Anime Recommender System 🎬

An intelligent anime recommendation system powered by LangChain, ChromaDB, and Groq LLM. This application uses vector embeddings and semantic search to provide personalized anime recommendations based on user preferences.

## Features

- **Semantic Search**: Uses vector embeddings to understand user preferences and find similar anime
- **LLM-Powered Recommendations**: Leverages Groq's LLM (Llama 3.1) for intelligent recommendation generation
- **Interactive Web Interface**: Built with Streamlit for an intuitive user experience
- **Vector Database**: ChromaDB for efficient similarity search and retrieval
- **Containerized Deployment**: Docker and Kubernetes support for production deployments
- **Logging & Error Handling**: Comprehensive logging and custom exception handling

## Tech Stack

- **LangChain**: Framework for building LLM applications
- **ChromaDB**: Vector database for embeddings storage and retrieval
- **Groq**: Fast LLM inference
- **Streamlit**: Web interface framework
- **Sentence Transformers**: For generating text embeddings
- **Docker & Kubernetes**: Container orchestration
- **Python 3.13**: Core programming language

## Project Structure

```
anime-recommender/
├── app/
│   └── app.py                  # Streamlit web application
├── config/
│   └── config.py              # Configuration and environment variables
├── data/
│   ├── anime_with_synopsis.csv # Raw anime data
│   └── processed_anime.csv     # Processed anime data
├── pipeline/
│   ├── build_pipeline.py       # Pipeline building utilities
│   └── pipeline.py             # Main recommendation pipeline
├── src/
│   ├── dataloader.py          # Data loading utilities
│   ├── prompt_template.py     # LLM prompt templates
│   ├── recommender.py         # Recommendation logic
│   └── vector_store.py        # Vector store operations
├── utils/
│   ├── custom_exceptions.py   # Custom exception classes
│   └── logger.py              # Logging configuration
├── chroma_db/                 # ChromaDB vector store
├── Dockerfile                 # Docker container configuration
├── llmops-k8s.yaml           # Kubernetes deployment config
├── pyproject.toml            # Project dependencies
└── requirements.txt          # Python dependencies
```

## Prerequisites

- Python 3.13 or higher
- API Keys:
  - Groq API key (get from [console.groq.com](https://console.groq.com))
  - Hugging Face API token (get from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens))
- Docker (optional, for containerized deployment)
- Kubernetes (optional, for K8s deployment)

## Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd anime-recommender
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # OR using uv
   uv sync
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   HUGGINGFACE_API_TOKEN=your_huggingface_token_here
   MODEL_NAME=llama-3.1-8b-instant
   EMBEDDING_MODEL_NAME=all-MiniLM-L6-v2
   VECTOR_STORE_PATH=chroma_db
   ```

5. **Build the vector store** (if not already built)
   ```bash
   python pipeline/build_pipeline.py
   ```

## Usage

### Running the Application

Start the Streamlit application:

```bash
streamlit run app/app.py
```

The application will be available at `http://localhost:8501`

### Using the Recommender

1. Open the web interface in your browser
2. Enter your anime preferences in the text input (e.g., "I like action anime with supernatural powers")
3. Click enter or wait for the recommendation to generate
4. View personalized anime recommendations based on your query

### Example Queries

- "I want a dark fantasy anime with complex characters"
- "Recommend me a slice of life anime about school life"
- "Looking for a mecha anime with emotional storylines"
- "Suggest anime similar to Attack on Titan"

## Docker Deployment

### Build the Docker image

```bash
docker build -t anime-recommender:latest .
```

### Run the container

```bash
docker run -p 8501:8501 \
  -e GROQ_API_KEY=your_api_key \
  -e HUGGINGFACE_API_TOKEN=your_token \
  -v $(pwd)/chroma_db:/app/chroma_db \
  anime-recommender:latest
```

Access the application at `http://localhost:8501`

## Kubernetes Deployment

Deploy to Kubernetes cluster:

```bash
# Create secrets for API keys
kubectl create secret generic anime-recommender-secrets \
  --from-literal=GROQ_API_KEY=your_api_key \
  --from-literal=HUGGINGFACE_API_TOKEN=your_token

# Apply the deployment
kubectl apply -f llmops-k8s.yaml

# Check deployment status
kubectl get pods
kubectl get services
```

## Architecture

The application follows a modular architecture:

1. **Data Layer**: CSV data loader and preprocessor
2. **Vector Store Layer**: ChromaDB for storing and retrieving anime embeddings
3. **Retrieval Layer**: Semantic search using sentence transformers
4. **LLM Layer**: Groq-powered language model for generating recommendations
5. **Application Layer**: Streamlit interface for user interaction

### Recommendation Pipeline

```
User Query → Embedding → Vector Search → Context Retrieval → LLM Processing → Recommendations
```

## Configuration

Key configurations in [config/config.py](config/config.py):

- `MODEL_NAME`: Groq LLM model (default: llama-3.1-8b-instant)
- `EMBEDDING_MODEL_NAME`: Sentence transformer model (default: all-MiniLM-L6-v2)
- `VECTOR_STORE_PATH`: ChromaDB persistence directory (default: chroma_db)

## Development

### Adding New Features

1. Data processing: Modify [src/dataloader.py](src/dataloader.py)
2. Prompts: Update [src/prompt_template.py](src/prompt_template.py)
3. Recommendation logic: Edit [src/recommender.py](src/recommender.py)
4. UI changes: Modify [app/app.py](app/app.py)

### Logging

Logs are stored in the `logs/` directory. Configure logging in [utils/logger.py](utils/logger.py).

## Troubleshooting

**Issue**: Missing API keys
- **Solution**: Ensure `.env` file is created with valid API keys

**Issue**: ChromaDB not found
- **Solution**: Run `python pipeline/build_pipeline.py` to build the vector store

**Issue**: Import errors
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

## License

This project is licensed under the MIT License.

## Acknowledgments

- Anime data sourced from publicly available datasets
- Built with LangChain framework
- Powered by Groq for fast LLM inference
- Vector embeddings by Hugging Face Sentence Transformers
