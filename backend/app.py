import asyncio
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from ai_connect import analisysAi

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/classificar', methods=['POST'])
def classificar():
    content = request.json
    email_content =  content.get("email")
    
    print(email_content);
    response_text = asyncio.run(analisysAi(email_content))
    response_json = json.loads(response_text)
    return response_json