# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

@app.route("/login", methods=['GET'])
def login():
    return "<h1>Usuario {0}</h1>".format(request.args.get('user')) 

if __name__ == "__main__":
    app.run(debug=True)
