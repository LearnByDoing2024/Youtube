from openai import OpenAI

# Initialize local LLM client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="your_lm_studio_api_key")

def generate_response(query):
    """Generate a response using the local language model."""
    try:
        response = client.chat.completions.create(
            model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
            messages=[
                {"role": "system", "content": "You are a professional GDPR advisor"},
                {"role": "user", "content": "I am a IT company and want to mitigate GDPR risk, what should I do./n "
                 "What are the penalties for non-compliance with GDPR?/n"  
                 "Use plain non legal tone. Do you have some examples./n"
                 "output with line changing sign for each point."}
            ],
         
            max_tokens=2000,
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def save_to_html(query, answer, filename='lmstudio_response.html'):
    """Save the query and response to an HTML file."""
    # Replace newlines in both query and answer with <br> tags
    query_with_line_breaks = query.replace('\n', '<br>')
    answer_with_line_breaks = answer.replace('\n', '<br>')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LM Studio Response</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            .query, .response {{ background-color: #f0f0f0; padding: 15px; border-radius: 8px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>LM Studio Query and Response</h1>
        <div class="query">
            <strong>Query:</strong>
            <p>{query_with_line_breaks}</p>
        </div>
        <div class="response">
            <strong>Response:</strong>
            <p>{answer_with_line_breaks}</p>
        </div>
    </body>
    </html>
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Report saved as {filename}")


if __name__ == "__main__":
    user_query = input("I am a IT company and want to mitigate GDPR risk, what should I do./n " "What are the penalties for non-compliance with GDPR?/n" "Use plain non legal tone. Do you have some examples./n" "output with line changing sign for each point.")
    response = generate_response(user_query)
    save_to_html(user_query, response)


#"I am a IT company and want to mitigate GDPR risk, what should I do./n " "What are the penalties for non-compliance with GDPR?/n" "Use plain non legal tone. Do you have some examples./n" "output with line changing sign for each point."}