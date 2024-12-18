
# AI Readiness

This project is a web application that evaluates AI readiness using a radar chart and integrates with OpenAI's GPT-3 to enhance the data.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/nesibekiris/ai-readiness.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ai-readiness
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set your OpenAI API key in `app.py`:
   ```python
   openai.api_key = 'your-openai-api-key'
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Check the boxes in each section to generate a radar map.
- Click "Submit to GPT" to send the data to the GPT-3 endpoint and receive an enhanced response.
