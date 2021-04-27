# Exercise 34

# script to create JSON file

import json

birthday_dictionary = {

"Richard Feynman": "11/05/1918",
"Albert Einstein": "14/03/1879",
"Isaac Newton": "04/01/1643",
"Stephen Hawking": "08/01/1942",
"Nikola Tesla": "10/07/1856"

}

with open("info.json", "w") as f:
    json.dump(birthday_dictionary, f)
