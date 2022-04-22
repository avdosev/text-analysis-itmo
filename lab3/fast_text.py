from common import *
import fasttext
import fasttext.util

words = load_words()

fasttext.util.download_model('ru', if_exists='ignore') 
ft = fasttext.load_model('cc.ru.300.bin')

wecs = ft.get_word_vector(words)

print('wecs:')
print(wecs[:10])