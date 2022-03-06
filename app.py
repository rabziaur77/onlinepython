from flask import Flask, jsonify
from converter import load_image_text_first_copy

app = Flask(__name__)


@app.route("/")
def index():
    response = load_image_text_first_copy("ss.PNG", True)
    return response


if __name__ == "__main__":
    app.run(debug=True)
