import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

UPLOAD_FOLDER = "static/screenshots"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Assignment 2 - Trojan Dashboard</title>
    <meta http-equiv="refresh" content="30">
    <style>
        body { font-family: sans-serif; text-align: center; background: #222; color: #fff; padding-top: 50px; }
        img { max-width: 80%; border: 3px solid #fff; box-shadow: 0px 0px 15px rgba(255,255,255,0.3); }
    </style>
</head>
<body>
    <h1>Live Target Screenshots</h1>
    <p>Refreshing automatically every 30 seconds...</p>
    <div>
        {% if latest_img %}
            <img src="{{ url_for('static', filename='screenshots/' + latest_img) }}" alt="Screenshot">
        {% else %}
            <p>Waiting for game data...</p>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/")
def index():
  files = os.listdir(UPLOAD_FOLDER)
  latest_img = None
  if files:
    files.sort(
        key=lambda x: os.path.getmtime(os.path.join(UPLOAD_FOLDER, x)),
        reverse=True,
    )
    latest_img = files[0]
  return render_template_string(HTML_PAGE, latest_img=latest_img)


@app.route("/upload", methods=["POST"])
def upload():
  if "screenshot" in request.files:
    file = request.files["screenshot"]
    file.save(os.path.join(UPLOAD_FOLDER, "latest.png"))
    return "Received", 200
  return "Failed", 400


if __name__ == "__main__":
  app.run(port=5000)