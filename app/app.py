import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from config.config import config

st.set_page_config(page_title="Anime Recommender", layout="wide", page_icon="🎬")

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline(persist_dir=config.VECTOR_STORE_PATH)

pipeline = init_pipeline()

st.title("Anime Recommender System")

user_query = st.text_input("Enter your anime preferences (e.g., genres, themes, etc.)") 

if user_query:
    with st.spinner("Fetching Recommendations for you ..."):
        response = pipeline.recommend(user_query)
        st.markdown("### Recommendations:")
        st.write(response)
