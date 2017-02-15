from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ''

@app.route("/new")
def new_note()

if __name__ == '__main__':
    app.debug = True
    app.run()