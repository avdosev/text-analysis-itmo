from common import *

with open('data/lab3_all_words.txt', 'w', encoding='utf-8') as f:
    for word in prepare_words():
        print(word, file=f)
