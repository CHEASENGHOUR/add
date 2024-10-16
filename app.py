from flask import Flask, request, jsonify, render_template
from langchain_ollama import OllamaLLM
# from flask_caching import Cache

app = Flask(__name__)
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# Ollama API URL for model interaction
# Initialize the Ollama LLM
ollama_llm = OllamaLLM(model="llama3.1")
# Change this to "llama3.1" if available

# Function to generate response using LangChain's OllamaLLM


# @cache.cached(timeout=60, query_string=True)
def ollama_generate(prompt):
    response = ollama_llm.invoke(prompt)
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']

    # Send the user message to Ollama and get the response
    ollama_response = ollama_generate(user_message)

    # Return Ollama's response as JSON
    return jsonify({'response': ollama_response})


if __name__ == '__main__':
    app.run(debug=True)
