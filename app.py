from flask import Flask, jsonify
import datetime
import platform
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🐳 Docker Lab 1 - Flask App</h1>
    <p>Welcome to my Dockerized Flask application!</p>
    <ul>
        <li><a href="/health">Health Check</a></li>
        <li><a href="/info">System Info</a></li>
        <li><a href="/time">Current Time</a></li>
    </ul>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "App is running successfully!"
    }), 200

@app.route("/info")
def info():
    return jsonify({
        "app": "Docker Lab 1",
        "python_version": sys.version,
        "platform": platform.system(),
        "architecture": platform.machine()
    })

@app.route("/time")
def current_time():
    return jsonify({
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "UTC"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)