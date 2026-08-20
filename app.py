from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/groq', methods=['POST'])
def groq_proxy():
    try:
        data = request.get_json()
        system_prompt = data.get('system', '')
        user_prompt = data.get('user', '')

        if not GROQ_API_KEY:
            return jsonify({'error': 'GROQ_API_KEY not set'}), 500

        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': 'openai/gpt-oss-120b',   # unchanged as requested
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ],
            'temperature': 0.7,
            'max_tokens': 3200
        }

        response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        content = result['choices'][0]['message']['content']
        return jsonify({'content': content})

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out. Please try again.'}), 504
    except requests.exceptions.RequestException as e:
        # log the full error for debugging
        print('Groq error:', e.response.text if e.response else str(e))
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        print('Unexpected error:', e)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
