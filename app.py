
from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enhance', methods=['POST'])
def enhance():
    data = request.get_json()
    prompt = f"Enhance the following data: {data}"
    
    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50
    )
    
    message = response.choices[0].text.strip()
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
