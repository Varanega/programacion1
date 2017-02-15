# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    print(request)
    print(request.path)
    print(request.method)
    print(request.form)
    return str(request)

if __name__ == "__main__":
    app.run(debug=True)
