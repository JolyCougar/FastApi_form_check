import json
import os.path
import logging
from pymongo import MongoClient, errors

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def get_db():
    """
    Подключаемся к MongoDB и возвращаем объект базы данных.
    """
    try:
        client = MongoClient(os.environ.get("MONGO_URL", "mongodb://localhost:27017/"))
        db = client["forms_db"]
        return db
    except errors.ConnectionFailure as e:
        logger.error(f"Ошибка подключения к базе данных MongoDB: {e}")
        raise


def insert_templates_to_db():
    """
    Загружаем шаблоны в базу данных
    """
    if not get_templates():
        db = get_db()
        templates_collection = db["templates"]
        try:
            with open("app/templates.json", "r") as f:
                templates_data = json.load(f)
        except FileNotFoundError:
            logger.error("Файл не найден")
        try:
            templates_collection.insert_many(templates_data, ordered=False)
            logger.info("Шаблоны успешно добавлены в базу данных.")
        except errors.BulkWriteError as e:
            logger.error(f"Ошибка при добавлении данных в базу данных: {e}")


def get_templates():
    """
    Получаем шаблоны из базы данных
    """
    db = get_db()
    templates_collection = db["templates"]

    templates = list(templates_collection.find())
    if templates:
        return templates
    else:
        logger.info('Шаблоны в БД отсутствуют')
