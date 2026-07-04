import json
import random

def get_daily_verse():

    with open("data/verses.json", "r", encoding="utf-8") as file:
        verses = json.load(file)

    return random.choice(verses)