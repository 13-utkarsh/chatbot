import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from groq import Groq
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question strictly based only on the following context:

{context}

---

Answer the question strictly based on the above context. Don't give any reply out of context: {question}
"""

# Initialize Groq client
GROQ_API_KEY = "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"  # Replace with your API key
groq_client = Groq(api_key=GROQ_API_KEY)

def query_rag(query_text: str):
    """Retrieves relevant context from ChromaDB and queries Groq's LLaMA 3."""

    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_score(query_text, k=10)
    print(f"\n--- Retrieval Results for '{query_text}' ---")
    for doc, score in results:
        print(f"Score: {score}\nContent: {doc.page_content}\nMetadata: {doc.metadata}\n---")

    if not results:
        return "No relevant documents found."

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE).format(
        context=context_text, question=query_text
    )
    print(f"\n--- Prompt Sent to Model ---:\n{prompt}")

    try:
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        response_text = response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

    sources = [doc.metadata.get("id", "Unknown Source") for doc, _ in results]
    return f"Response: {response_text}\nSources: {sources}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query the RAG chatbot.")
    parser.add_argument("query_text", type=str, help="The input query text.")
    args = parser.parse_args()
    print(query_rag(args.query_text))
