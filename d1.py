import json
from difflib import get_close_matches
import keyword

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word,data.keys()))>0:
        yn=raw_input("Did you mean %s insead? Enter Y or y if yes , N or n if no: "%get_close_matches(word,data.keys())[0])
        if yn=="Y" or yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N" or yn=="n":
            return "Word not found!"
        else:
            return "Don't recognize your entry!!!"
    else:
        return "Word not found!!!!"

word=raw_input("Enter word to serach: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
