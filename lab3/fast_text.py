from common import *
import fasttext
import fasttext.util
import sklearn
from sklearn.cluster import DBSCAN as dbscan
import json
import joblib

words = load_words()

fasttext.util.download_model('ru', if_exists='ignore') 
ft = fasttext.load_model('cc.ru.300.bin')

print('transform to vectors')
vecs = [ft.get_word_vector(word) for word in words]

# print(words[0], vecs[0])
print('fit clusters')

compute_clusters = True
# compute_clusters = False
if compute_clusters:
    with open('lab3/data/fast_text_clusters.pkl', 'wb') as f:
        clusters = dbscan()
        clusters.fit(vecs)
        joblib.dump(clusters, f)
else:
    with open('lab3/data/fast_text_clusters.pkl', 'rb') as f:
        clusters = joblib.load(f)

drop_clusters = True
# drop_clusters = False
if drop_clusters:
    print('drop clusters')

    with open('lab3/data/fast_text_data.json', 'w', encoding='utf-8') as f:
        data = {data[0]: {'label': data[0], 'cluster': int(data[1])}for data in zip(words, clusters.labels_)}
        json.dump(data, f)
