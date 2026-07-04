import json

def get_verse(mood):

    with open("data/verses.json", "r", encoding="utf-8") as file:
        verses = json.load(file)

    for verse in verses:
        if verse["topic"] == mood:
            return verse

    return verses[-1]