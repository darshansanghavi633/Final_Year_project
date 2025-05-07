from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from models_utils import generate_linkedin_post, extract_keywords_yake

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/generate-caption', methods=['POST'])
def generate_caption():
    data = request.get_json()
    topic = data.get("topic", "")
    
    if not topic:
        return jsonify({"error": "Topic is required"}), 400
    
    keywords = extract_keywords_yake(topic)
    post = generate_linkedin_post(topic, keywords)
    
    return jsonify({"post": post})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
