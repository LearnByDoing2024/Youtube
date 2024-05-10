import pandas as pd
import pdfplumber
import nltk
import tensorflow_hub as hub
import numpy as np
from openai import OpenAI
import tensorflow as tf
import os as os
from numpy.linalg import norm


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
        # Calculate cosine similarity between the query embedding and all stored embeddings
        similarities = [np.dot(query_embedding, doc_emb) / (norm(query_embedding) * norm(doc_emb)) for doc_emb in self.embeddings]
        
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

def csv_to_text(filenames, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as output_file:  # Specify UTF-8 encoding
        for filename in filenames:
            df = pd.read_csv(filename)
            for index, row in df.iterrows():
                # Convert each row to a string format with desired formatting
                output_file.write(' '.join(str(x) for x in row) + '\n')

def load_and_extract_text(file_path):
    # Determine the file extension
    _, file_extension = os.path.splitext(file_path)
    text_content = []
    
    if file_extension.lower() == '.pdf':
        # Process as PDF
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_content.append(text)
    elif file_extension.lower() in ['.txt', '.text']:
        # Process as Text
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content.append(file.read())
    else:
        raise ValueError("Unsupported file type")

    return " ".join(text_content)

def nltk_sentence_splitter(text):
    return nltk.tokenize.sent_tokenize(text)

def load_and_split_text(file_path):
    document_text = load_and_extract_text(file_path)
    return nltk_sentence_splitter(document_text)

def setup_vector_store_1(text_chunks_1):
    vector_store_1 = SimpleVectorStore()
    embeddings = embed_text(text_chunks_1)
    for chunk, embedding in zip(text_chunks_1, embeddings):
        vector_store_1.add_document(embedding, chunk)
    return vector_store_1

def setup_vector_store_2(text_chunks_2):
    additional_embeddings = embed_text(text_chunks_2)
    vector_store_2 = SimpleVectorStore()
    for additional_chunk, additional_embedding in zip(text_chunks_2, additional_embeddings):
        vector_store_2.add_document(additional_embedding, additional_chunk)
    
    return vector_store_2


# Local LLM setup
client = OpenAI(base_url="http://localhost:1234/v1", api_key="your_lm_studio_api_key")

def generate_response(query, vector_store_1, vector_store_2):
    query_embedding = embed_text([query])[0]
    similar_docs_1 = vector_store_1.search(query_embedding)
    similar_docs_2 = vector_store_2.search(query_embedding)
    prompt = " ".join(similar_docs_1) .join(similar_docs_2) + "\n\n" + query
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
        {"role": "system", "content": "You are a professional GDPR advisor, specialized in GDPR compliance analysis, plan drafting, report generation"},
        {"role": "user", "content": prompt}
            ],
        temperature=0.1,
        max_tokens=1000,
        presence_penalty=2, 
        frequency_penalty=2      
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

def save_debug_info_to_html(gdpr_data, gdpr_text_chunks, vector_store_1, vector_store_2, user_query, final_answer, filename='debug_report.html'):
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
            <pre>{'\\n'.join(vector_store_1.documents[:5])}</pre>
        </div>
        <div class="section">
            <h2>First few documents stored:</h2>
            <pre>{'\\n'.join(vector_store_2.documents[:5])}</pre>
        </div>
        <div class="section">
            <h2>First few embeddings stored:</h2>
            <pre>{vector_store_1.embeddings[:5]}</pre>
        </div>
        <div class="section">
            <h2>First few embeddings stored:</h2>
            <pre>{vector_store_2.embeddings[:5]}</pre>
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
    gdpr_data_text = csv_to_text(['gdpr_fines.csv', 'gdpr_fines_wiki_0.csv'], 'output.txt')
    gdpr_text_chunks = load_and_split_text('CELEX_32016R0679_EN_TXT.pdf')
    gdpr_data_text_chunks = load_and_split_text('output.txt')
    vector_store_1 = setup_vector_store_1(gdpr_text_chunks) # Change here 
    vector_store_2 = setup_vector_store_2(gdpr_data_text_chunks)
    user_query = (
                  "I am an IT company and want to mitigate GDPR risk, what should I do." 
                  "What are the penalties for non-compliance with GDPR?/n" "Use plain non legal tone. Do you have some examples." 
                  " Provide a comprehensive report."                  
                )
    #output with line changing sign for each point.
    #"stop output when repetition begins."
    final_answer = generate_response(user_query, vector_store_1, vector_store_2)
    print(final_answer)
    # Save the query and response to an HTML file
    save_to_html(user_query, final_answer)
    save_debug_info_to_html(gdpr_data, gdpr_text_chunks, vector_store_1, vector_store_2, user_query, final_answer)

