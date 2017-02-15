from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><strong> Mi gato</strong> es bonito</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run()