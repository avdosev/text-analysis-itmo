# for run use pypy3

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
    for i in range(-n_grams+1, len(text)+n_grams-1):
        words = []
        for j in range(i, i+n_grams):
            if j < 0: words.append(START_SEQ)
            elif j >= len(text): words.append(END_SEQ)
            else: words.append(text[j])
        yield words
    yield text[-(n_grams-1):] + [END_SEQ]

for item in counts.items():
    result[item[0]] = item[1] / len(all_words)

def save_n_gramm(n):
    print('n-grams', n)

    n_gram_counts = Counter()
    for text in texts:
        n_gram_counts.update(['~'.join(n_gram) for n_gram in make_n_gram(text, n)])
    
    counts.update(n_gram_counts)
    counts.update({'~'.join([END_SEQ]*(n-1)): len(texts)})
    counts.update({'~'.join([START_SEQ]*(n-1)): len(texts)})

    new_result = {}
    k = 0.001
    v = sum(n_gram_counts.values())
    print(f'v={v}')
    for n_gram, count in n_gram_counts.items():
        i = n_gram.rfind('~')
        word, u_gram  = n_gram[:i], n_gram[i+1:]
        try:
            new_result[n_gram] = (count + k) / (counts[word] + k*v)
        except ZeroDivisionError:
            print(n_gram)

    with open(f'lab2/cache/data_{n}.json', 'w', encoding='utf-8') as f:
        json.dump(new_result, f, ensure_ascii=False, indent=1)

for n in range(2, 6):
    save_n_gramm(n)