import pandas as pd
import pdfplumber
import nltk
import tensorflow_hub as hub
import numpy as np
from openai import OpenAI

# Ensure nltk resources are available
nltk.download('punkt')

class SimpleVectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = []

    def add_document(self, embedding, document):
        self.embeddings.append(embedding)
        self.documents.append(document)

    def search(self, query_embedding, top_k=5):
        # Naive search: returns the first `top_k` documents
        return self.documents[:top_k]

# Load Google's Universal Sentence Encoder
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def embed_text(text_chunks):
    # Embeds text using Google's Universal Sentence Encoder
    return embed(text_chunks).numpy()

def load_csv_data(filenames):
    return pd.concat([pd.read_csv(f) for f in filenames])

def load_and_extract_text_from_pdf(file_path):
    text_content = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_content.append(text)
    return " ".join(text_content)

def nltk_sentence_splitter(text):
    return nltk.tokenize.sent_tokenize(text)

def load_and_split_text(file_path):
    document_text = load_and_extract_text_from_pdf(file_path)
    return nltk_sentence_splitter(document_text)

def setup_vector_store(text_chunks):
    vector_store = SimpleVectorStore()
    embeddings = embed_text(text_chunks)
    for chunk, embedding in zip(text_chunks, embeddings):
        vector_store.add_document(embedding, chunk)
    return vector_store

# Local LLM setup
client = OpenAI(base_url="http://localhost:1234/v1", api_key="your_lm_studio_api_key")

def generate_response(query, vector_store):
    query_embedding = embed_text([query])[0]
    similar_docs = vector_store.search(query_embedding)
    prompt = " ".join(similar_docs) + "\n\n" + query
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
        {"role": "system", "content": "You are a professional GDPR advisor"},
        {"role": "user", "content": f"I am a IT company and want to mitigate GDPR risk, /n"
         "what should I do. What are the penalties for non-compliance with GDPR?  Use plain non legal tone. /n"
         "Do you have some examples. {prompt}"}
            ],
        temperature=0.1,
        max_tokens=2000
    )
    return completion.choices[0].message.content

def save_to_html(query, answer, filename='gdpr_compliance_report.html'):
    # Replace newlines in the answer with <br> tags
    answer_with_line_breaks = answer.replace('\n', '<br>')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GDPR Compliance Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            p {{ color: #666; }}
            .query {{ background-color: #f4f4f9; padding: 10px; border-radius: 8px; margin-top: 20px; }}
            .response {{ background-color: #e2f4f1; padding: 10px; border-radius: 8px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>GDPR Compliance Inquiry</h1>
        <div class="query">
            <h2>Query:</h2>
            <p>{query}</p>
        </div>
        <div class="response">
            <h2>Response:</h2>
            <p>{answer_with_line_breaks}</p>
        </div>
    </body>
    </html>
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Report saved to {filename}")


# Main execution
if __name__ == "__main__":
    gdpr_data = load_csv_data(['gdpr_fines.csv', 'gdpr_fines_wiki_0.csv'])
    gdpr_text_chunks = load_and_split_text('CELEX_32016R0679_EN_TXT.pdf')
    vector_store = setup_vector_store(gdpr_text_chunks)
    user_query = "I am a IT company and want to mitigate GDPR risk, what should I do./n " "What are the penalties for non-compliance with GDPR?/n" "Use plain non legal tone. Do you have some examples./n" "output with line changing sign for each point."
    final_answer = generate_response(user_query, vector_store)
    print(final_answer)
    # Save the query and response to an HTML file
    save_to_html(user_query, final_answer)
