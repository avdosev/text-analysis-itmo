import json
import os
import re

data_path = 'data/out/AA'

texts = []

for file_name in os.listdir(data_path):
    print('preparing: {}'.format(file_name))
    with open(os.path.join(data_path,file_name)) as f:
        lines = f.readlines()
        for line in lines:
            text = json.loads(line)['text']
            texts.append(text)

# подготовить тексты 
# разбить на слова
uniques_words = set()
sep = re.compile(r'\W+') 
notRussia = re.compile(r'[^а-я]') 
for i, text in enumerate(texts):
    words = re.split(sep, text)
    words = [s.lower() for s in words if len(s) != 0]
    # неплохо бы использоваться pymorphy
    uniques_words.update(words)

def need_skip(word: str):
    return notRussia.search(word) is not None

uniques_words = [word for word in uniques_words if not need_skip(word)] 
uniques_words.sort()

print()
print('Первый десяток слов')
print(uniques_words[:10])


# сделать предвычисления
# сохранить в папку lab1/cahce
with open('lab1/cache/words.txt', 'w', encoding='utf-8') as f:
    for word in uniques_words:
        try:
            print(word, file=f)
        finally:
            None
