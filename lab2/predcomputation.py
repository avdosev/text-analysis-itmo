import json

from collections import Counter


filename = 'lab2/cache/texts.json'

with open(filename, encoding='utf-8') as f:
    texts = json.load(f)

result = {}
all_words = [word for text in texts for word in text]
counts = Counter(all_words)

# убрать эту хрень и добавить расчет биграм
for item in counts.items():
    result[item[0]] = item[1] / len(all_words)

with open('lab2/cache/data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False)