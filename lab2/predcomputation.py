# for run use pypy3
import io
import sys
sys.stdout = io.open(sys.stdout.fileno(), 'w', encoding='cp1251')
import json
from collections import Counter


filename = 'cache/train.json'
START_SEQ = '__start_seq'
END_SEQ = '__end_seq'

with open(filename, encoding='utf-8') as f:
    texts = json.load(f)

result = {}
all_words = [word for text in texts for word in text]
counts = Counter(all_words)
v = len(all_words)

def make_n_gram(text, n_grams):
    for i in range(-n_grams+1, len(text)):
        words = []
        for j in range(i, i+n_grams):
            if j < 0: words.append(START_SEQ)
            elif j >= len(text): words.append(END_SEQ)
            else: words.append(text[j])
        yield words

for item in counts.items():
    result[item[0]] = item[1] / v

# with open(f'cache/data.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False, indent=1)

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
    for n_gram, count in n_gram_counts.items():
        i = n_gram.rfind('~')
        word, u_gram  = n_gram[:i], n_gram[i+1:]
        try:
            # мусор получается -> значения стремятся к какому-то одному числу
            # new_result[n_gram] = (count + k) / (counts[word] + k*v)
            new_result[n_gram] = ( count+k ) / (counts[word] + k)
        except ZeroDivisionError:
            print(n_gram)
    result.update(new_result)
    # with open(f'cache/data.json', 'w', encoding='utf-8') as f:
    #     json.dump(new_result, f, ensure_ascii=False, indent=1)

for n in range(2, 6):
    # print(list(make_n_gram(['1', '2', '3', '4', '5', '6'], n)))
    save_n_gramm(n)

with open(f'cache/data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)