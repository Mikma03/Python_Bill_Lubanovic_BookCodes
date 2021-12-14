from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Strona żyje!"

app.run(debug=True)
