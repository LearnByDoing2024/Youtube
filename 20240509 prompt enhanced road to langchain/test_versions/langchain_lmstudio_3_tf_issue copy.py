import pandas as pd
import pdfplumber
import nltk
import tensorflow_hub as hub
import numpy as np
from openai import OpenAI
import tensorflow as tf

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
        # Ensure that query_embedding is a NumPy array
        query_embedding = np.array(query_embedding)
        # Calculate cosine similarity between the query embedding and all stored embeddings
        similarities = [np.dot(query_embedding, doc_emb) / (np.norm(query_embedding) * np.norm(doc_emb)) for doc_emb in self.embeddings]
        # Get the indices of the top_k documents with the highest similarity scores
        top_k_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:top_k]
        # Return the corresponding top_k documents
        return [self.documents[i] for i in top_k_indices]

# Load Google's Universal Sentence Encoder
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def embed_text(text_chunks):
    # Ensure text_chunks is a list of strings
    if not all(isinstance(chunk, str) for chunk in text_chunks):
        raise ValueError("All text chunks must be strings.")
    # Convert text list to TensorFlow tensors and get embeddings
    text_tensors = tf.convert_to_tensor(text_chunks, dtype=tf.string)
    return embed(text_tensors).numpy()


def load_csv_data(filenames):
    # Concatenate all CSV files into a single DataFrame
    dataframes = [pd.read_csv(f) for f in filenames]
    combined_df = pd.concat(dataframes)
    # Replace all NaN values with 0
    combined_df.fillna(0, inplace=True)
    # Convert all int columns to float
    for col in combined_df.select_dtypes(include=['int', 'int64']):
        combined_df[col] = combined_df[col].astype(float)
    return combined_df


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

def setup_vector_store(text_chunks, data1):
    vector_store = SimpleVectorStore()
    embeddings = embed_text(text_chunks)
    for chunk, embedding in zip(text_chunks, embeddings):
        vector_store.add_document(embedding, chunk)
    
    additional_embeddings = embed_text(data1)
    for additional_chunk, additional_embedding in zip(data1, additional_embeddings):
        vector_store.add_document(additional_embedding, additional_chunk)
    
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
        {"role": "user", "content": prompt}
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

def save_debug_info_to_html(gdpr_data, gdpr_text_chunks, vector_store, user_query, final_answer, filename='debug_report.html'):
    # Create HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Debug Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1, h2 {{ color: #333; }}
            p, pre {{ color: #666; }}
            .section {{ background-color: #f4f4f9; padding: 10px; border-radius: 8px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>Debugging Report</h1>
        <div class="section">
            <h2>GDPR Data DataFrame:</h2>
            <pre>{gdpr_data.to_html()}</pre>
        </div>
        <div class="section">
            <h2>First few sentences from the PDF:</h2>
            <pre>{'\\n'.join(gdpr_text_chunks[:5])}</pre>
        </div>
        <div class="section">
            <h2>First few documents stored:</h2>
            <pre>{'\\n'.join(vector_store.documents[:5])}</pre>
        </div>
        <div class="section">
            <h2>First few embeddings stored:</h2>
            <pre>{vector_store.embeddings[:5]}</pre>
        </div>
        <div class="section">
            <h2>Query:</h2>
            <pre>{user_query}</pre>
        </div>
        <div class="section">
            <h2>Generated response:</h2>
            <pre>{final_answer}</pre>
        </div>
    </body>
    </html>
    """
    # Write to HTML file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Report saved to {filename}")


# Main execution
if __name__ == "__main__":
    gdpr_data = load_csv_data(['gdpr_fines.csv', 'gdpr_fines_wiki_0.csv'])
    gdpr_text_chunks = load_and_split_text('CELEX_32016R0679_EN_TXT.pdf')
    vector_store = setup_vector_store(gdpr_text_chunks, gdpr_data) # Change here
    user_query = "I am an IT company and want to mitigate GDPR risk, what should I do./n " "What are the penalties for non-compliance with GDPR?/n" "Use plain non legal tone. Do you have some examples./n" "output with line changing sign for each point."
    final_answer = generate_response(user_query, vector_store)
    print(final_answer)
    # Save the query and response to an HTML file
    save_to_html(user_query, final_answer)
    save_debug_info_to_html(gdpr_data, gdpr_text_chunks, vector_store, user_query, final_answer)

