import json
import random

test_filename = 'lab2/cache/test.json'
model_filename = 'lab2/cache/data.json'

with open(test_filename, encoding='utf-8') as f:
    texts = json.load(f)

with open(model_filename, encoding='utf-8') as f:
    probability = json.load(f)


eps = 0.01
text_amount = 100


def eval_perplexity(gram_size):
    avg = 0
    for iter in range(text_amount):
        text = texts[random.randint(0, len(texts))]
        mul = 1
        for id in range(1, len(text)+1):
            if id - gram_size >= 0:
                key = '~'.join(text[id - gram_size:id])
            else:
                key = '~'.join(text[0:id])
            if key in probability:
                mul *= probability[key] ** (-1. / len(text))
            else:
                mul *= eps ** (-1. / len(text))
        avg += mul
    return avg / text_amount


for n in range(2, 6):
    print(n, "gram perplexity = ", eval_perplexity(n))
