import json
import re
import html

filename = 'data/aneks.sql'

result = {}
dots = re.compile(r'\.{2,}')
aneks = []
with open(filename, encoding='utf-8') as f:
    for line in f:
        if not line.startswith('INSERT'):
            continue

        start = line.find("'")
        end = line.find("'", start+1)

        anek = line[start+1:end]
        anek = html.unescape(anek)
        try:
            anek = re.sub(dots, '.', anek)
        except:
            pass
        anek = anek.replace('\\n', ' ').lower()

        aneks.append(anek)

tokens = re.compile(r'(((\w\.)*\w+)|([,:\-?]|\.+))')

def tokenize(line: str):
    return [item[0] for item in re.findall(tokens, line)]

tokenized_aneks = [tokenize(anek) for anek in aneks]
def is_empty(sized): return len(sized) == 0
tokenized_aneks = [tokens for tokens in tokenized_aneks if not is_empty(tokens)]

result = tokenized_aneks
with open('lab2/cache/texts.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)




