# Simulation Database

from genericpath import exists
import json
from pathlib import Path

def create_db_if_not_exists():
    if not exists('./flashcards_db.json'):
        with open('./flashcards_db.json', 'w+') as f:
            f.write('[]')


def load_db():
    create_db_if_not_exists()
    with open('./flashcards_db.json') as f:
        return json.load(f)


def save_db():
    with open('./flashcards_db.json', 'w') as f:
        return json.dump(db, f)

db = load_db()