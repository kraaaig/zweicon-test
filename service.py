#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(message="hello world", date=datetime.now())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
