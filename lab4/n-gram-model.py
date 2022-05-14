from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

import os
os.chdir('C:/projects/itmo/text-anal/')

sentiment_to_num = {'negative': 0, 'neutral': 1, 'positive': 2}
n_gram = 2

test_csv = pd.read_csv('data/tweets_test.csv')
train_csv = pd.read_csv('data/tweets_train.csv')

train_X = train_csv['text']
train_y = train_csv['sentiment']

test_id = test_csv['textID']
test_X = test_csv['text']

tf_vectorizer = CountVectorizer(ngram_range=(n_gram, n_gram), lowercase=True)

X_train_tf = tf_vectorizer.fit_transform(train_X)


# matrix = X_train_tf.toarray()

# grams = tf_vectorizer.get_feature_names()
grams = tf_vectorizer.get_feature_names_out()

# grams_freq = X_train_tf.toarray().sum(axis=0)
grams_freq = np.asarray(X_train_tf.sum(axis=0))

grams_freq_dict = dict(zip(grams, grams_freq))

print('grams_freq_dict ready')

gram_split_freq = dict()

text_len = len(train_X)
grams_len = len(grams)

for i,j in zip(*X_train_tf.nonzero()):
    cur_gram = grams[j]
    if cur_gram not in gram_split_freq:
        gram_split_freq[cur_gram] = [0, 0, 0]
    
    gram_freq_per_doc = X_train_tf[i,j]
    gram_split_freq[cur_gram][sentiment_to_num[train_y[i]]] += gram_freq_per_doc

print('individual freq evaluation finished')
print('my_new freqs = ', gram_split_freq['my_new'])

y_pred = []

for text in test_X:
    cur_vec = CountVectorizer(ngram_range=(n_gram, n_gram), lowercase=True)
    cur_train = cur_vec.fit_transform(text)
    cur_grams = cur_vec.get_feature_names()
    freqs = []
    for id in range(0, 3):
        freq = 0.0
        for gram in cur_grams:
            total_freq = grams_freq_dict[gram]
            class_freq = gram_split_freq[gram][id]
            freq += class_freq / total_freq
        freqs.append(freq)
    final_class = ''
    if freqs[0] >= freqs[1] and freqs[0] >= freqs[2]:
        final_class = 'negative'
    if freqs[1] >= freqs[0] and freqs[1] >= freqs[2]:
        final_class = 'neutral'
    if freqs[2] >= freqs[0] and freqs[2] >= freqs[1]:
        final_class = 'positive'
    y_pred.append(final_class)

print('dump data to csv')

csv_dict = {'textID': test_id, 'sentiment': y_pred}
csv_df = pd.DataFrame(csv_dict)
csv_df.to_csv('data/my_submission_2_gram.csv', sep=',', encoding='utf-8', index=False)
