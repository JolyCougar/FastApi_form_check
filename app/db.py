import json
from pymongo import MongoClient


def get_db():
    client = MongoClient("mongodb://mongo:27017/")
    db = client["forms_db"]
    return db


def get_templates():
    with open("app/templates.json", "r") as f:
        return json.load(f)
