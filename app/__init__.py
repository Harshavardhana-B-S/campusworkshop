"""Setup at app startup"""
from flask import Flask
import psycopg2

app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa9m67avj5o48g5330-a.oregon-postgres.render.com",
        database="todo_9l3p",
        user="root",
        password="XkRZDbVzqUtKcZHY46mnb9wR6QDuM2mf")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
