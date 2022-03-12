import json

from collections import Counter


filename = 'lab2/cache/texts.json'
START_SEQ = '__start_seq'
END_SEQ = '__end_seq'

with open(filename, encoding='utf-8') as f:
    texts = json.load(f)

result = {}
all_words = [word for text in texts for word in text]
counts = Counter(all_words)

def make_n_gram(text, n_grams):
    for i in range(len(text)):
        words = []
        for j in range(i-n_grams//2, i+n_grams//2+n_grams%2):
            if j < 0: words.append(START_SEQ)
            elif j >= len(text): words.append(END_SEQ)
            else: words.append(text[j])
        yield words
    yield text[-(n_grams-1):] + [END_SEQ]

for item in counts.items():
    result[item[0]] = item[1] / len(all_words)

n_gram_counts = Counter()
for text in texts:
    n_gram_counts.update(['~'.join(n_gram) for n_gram in make_n_gram(text, 2)])
counts.update(n_gram_counts)
counts.update({END_SEQ: len(texts)})
counts.update({START_SEQ: len(texts)})

for n_gram, count in n_gram_counts.items():
    i = n_gram.find('~')
    word, u_gram = n_gram[:i], n_gram[i+1:]
    result[n_gram] = count / counts[word]

with open('lab2/cache/data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)

# есть смысл сформировать более удобное представление данных