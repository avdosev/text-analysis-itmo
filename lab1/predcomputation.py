from json import dump


path = 'lab1/cache'
words = []
with open(f'{path}/words.txt', encoding='utf-8') as f:
    words = f.read().splitlines()

result = {}

for word in words:
    chars = ''.join(sorted(set(word)))
    if chars not in result:
        result[chars] = []
    result[chars].append(word)

with open(f'{path}/data.json', 'w') as f:
    dump(result, f, indent=2)

