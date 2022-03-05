import json
import re

filename = 'data/aneks.sql'

result = {}
aneks = []
with open(filename, encoding='utf-8') as f:
    for line in f:
        if not line.startswith('INSERT'):
            continue

        start = line.find("'")
        end = line.find("'", start+1)

        anek = line[start+1:end]

        anek = anek.replace('\\n', '').lower()

        aneks.append(anek)

tokens = re.compile(r'((\w\.)*\w+)|([,:\-?]|\.+)')
def use_token(token): 
    if len(token[0]) == 0: return token[2]
    else: return token[0] 
def tokenize(line: str):
    return [use_token(item) for item in re.findall(tokens, line)]

tokenized_aneks = [tokenize(anek) for anek in aneks[:2]]

result = tokenized_aneks
with open('lab2/cache/data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)




