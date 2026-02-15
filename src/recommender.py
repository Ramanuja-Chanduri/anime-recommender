from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0.0)
        self.prompt = get_anime_prompt()

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        self.document_chain = self.prompt | self.llm | StrOutputParser()

        self.qa_chain = (
            RunnableParallel(
                {
                    "question": RunnablePassthrough(),
                    "source_documents": retriever,
                }
            ).assign(context=lambda x: format_docs(x["source_documents"]))
            | RunnableParallel(
                {
                    "result": self.document_chain,
                    "source_documents": lambda x: x["source_documents"],
                    "question": lambda x: x["question"],
                }
            )
        )
    
    def get_recommendation(self, query: str):
        result = self.qa_chain.invoke(query)
        return result["result"]
