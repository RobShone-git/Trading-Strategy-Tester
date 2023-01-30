import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def clean(x): ## Takes out rubbish and "."
    cur = str(x)[24:-6]
    out = ""
    for idx in range(len(cur)):
        if cur[idx] != ".":
            out += cur[idx]
    return out + symbol(x)

def symbol(y): ## Adds amount of '0' depending on symbol
    cur = str(y)[-6]
    if "." not in str(y):
        decimal = 0
    else:
        decimal = (str(y).index(cur)) - (str(y).index(".") + 1)
    out = ""
    if cur == "B":
        while 9 - decimal != 0:
            out += "0"
            decimal += 1
        return out
    elif cur == "M":
        while 6 - decimal != 0:
            out += "0"
            decimal += 1
        return out
    elif cur == "K":
        while 3 - decimal != 0:
            out += "0"
            decimal += 1
        return out
    else:
        return " New symbol"

my_dict = {}
url = "https://cryptofees.info/api/v1/fees"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
cur = json.loads(str(soup))
tokens = cur["protocols"]
for x in range(len(tokens)):
    tok = tokens[x]
    id = tok["id"]
    df = tok["fees"]
    seven_day = 0
    for x in range(len(df)):
        seven_day += df[x]["fee"]
    my_dict[id] = seven_day

print(my_dict)
