#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point module for the flask app
"""

from flask import (
    Flask,
    render_template,
)
from flask_pymongo import PyMongo
from datetime import datetime

SIMPLE = Flask(__name__)
SIMPLE.config['MONGO_HOST'] = '192.168.50.12'

MONGO = PyMongo(SIMPLE)


@SIMPLE.route('/')
def hello_world():
    try:
        last_access = MONGO.db.access.find_one({}, None, sort=[("$natural", -1)])
    except:
        MONGO.db.access.insert_one({
            "datetime": datetime.now(),
            "consecutive": 0,
        })
    finally:
        last_access = MONGO.db.access.find_one({}, None, sort=[("$natural", -1)])

    # Insert one right now
    MONGO.db.access.insert_one({
        "datetime": datetime.now(),
        "consecutive": last_access["consecutive"] + 1,
    })

    stats = MONGO.db.command("collstats", "access")

    return render_template(
        'index.html',
        stats=stats,
        last_access=last_access,
    )
