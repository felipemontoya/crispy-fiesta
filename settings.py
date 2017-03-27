#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Settings for simpleapp
"""
import os


class Config(object):
    DEBUG = os.environ.get("SIMPLE_DEBUG", False)
    TESTING = os.environ.get("SIMPLE_TESTING", False)
    MONGO_HOST = os.environ.get("SIMPLE_MONGO_HOST", "localhost")
