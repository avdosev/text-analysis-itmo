import json
import random

test_filename = 'cache/test.json'
model_filename = 'cache/data.json'

with open(test_filename, encoding='utf-8') as f:
    texts = json.load(f)

with open(model_filename, encoding='utf-8') as f:
    probability = json.load(f)


eps = 0.1
text_amount = 10


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
                mul *= probability[key]
            else:
                mul *= eps
        avg += (1. / mul) ** (1. / gram_size)
    return avg / text_amount


for n in range(2, 6):
    print(eval_perplexity(n))
