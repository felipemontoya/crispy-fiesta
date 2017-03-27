#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point module for the flask app
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
