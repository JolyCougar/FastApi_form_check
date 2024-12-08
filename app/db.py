import json
from pymongo import MongoClient, errors


def get_db():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["forms_db"]
        return db
    except errors.ConnectionFailure as e:
        print(f"Ошибка подключения к базе данных MongoDB: {e}")
        raise


def insert_templates_to_db():
    db = get_db()
    templates_collection = db["templates"]
    with open("app/templates.json", "r") as f:
        templates_data = json.load(f)
    try:
        templates_collection.insert_many(templates_data, ordered=False)
        print("Шаблоны успешно добавлены в базу данных.")
    except errors.BulkWriteError as e:
        print(f"Ошибка при добавлении данных в базу данных: {e}")

    return templates_data


def get_templates():
    db = get_db()
    templates_collection = db["templates"]

    templates = list(templates_collection.find())
    if templates:
        return templates
    else:
        insert_templates_to_db()



