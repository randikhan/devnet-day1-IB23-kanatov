from flask import Flask
import os
import hashlib

app = Flask(__name__)

token = os.getenv("STUDENT_TOKEN", "")
token_hash8 = hashlib.sha256(token.encode()).hexdigest()[:8] if token else ""

@app.route("/")
def home():
    return f"Hello Day4 | TOKEN_HASH8={token_hash8}"

app.run(host="0.0.0.0", port=8080, threaded=False)