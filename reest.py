# -*- coding: utf-8 -*-
"""
Created on Sun May 17 08:31:41 2020

@author: quantum
"""

from flask import Flask ,jsonify
reest = Flask(__name__)


@reest.route('/')
def hello():
    return <h1>"Hello World!"</h1>

@reest.route('/hello')
def realhello():
    return jsonify({"lemon":"Hello World!"}),201

if __name__ == '__main__':
    reest.run()