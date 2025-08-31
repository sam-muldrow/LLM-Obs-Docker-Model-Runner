import os
import json
import requests
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from ddtrace.llmobs import LLMObs


MODEL = os.getenv("LLM_MODEL_NAME")

LLMObs.enable(
  ml_app="llm_chat_bot",
  api_key=os.getenv("DD_API_KEY"),
  agentless_enabled=True,
)

app = Flask(__name__)
client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key="fake_api_key")

def get_model_name():
    """Returns the model name to use for API requests"""
    return MODEL

@app.route('/')
def index():
    """Serves the chat web interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat_api():
    """Processes chat API requests"""
    data = request.json
    message = data.get('message', '')

    # Special command for getting model info
    if message == "!modelinfo":
        return jsonify({'model': get_model_name()})

    # Call the LLM API
    try:
        response = call_llm_api(message)
        return jsonify({'response': response})
    except Exception as e:
        app.logger.error(f"Error calling LLM API: {e}")
        return jsonify({'error': 'Failed to get response from LLM'}), 500

def call_llm_api(user_message):
    """Calls the LLM API and returns the response"""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8081))

    print(f"Server starting on http://localhost:{port}")
    print(f"Using LLM endpoint: {os.getenv('LLM_BASE_URL', 'http://localhost:11434/v1')}")
    print(f"Using model: {os.getenv('LLM_MODEL_NAME', 'llama2')}")

    app.run(host='0.0.0.0', port=port, debug=os.getenv("DEBUG", "false").lower() == "true")
