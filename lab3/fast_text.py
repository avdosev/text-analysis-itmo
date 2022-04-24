from common import *
import fasttext
import fasttext.util
import sklearn
from sklearn.cluster import DBSCAN as dbscan
import json
import joblib
from collections import Counter

words = load_words()[:20000]

fasttext.util.download_model('ru', if_exists='ignore') 
ft = fasttext.load_model('cc.ru.300.bin')

print('transform to vectors')
vecs = [ft.get_word_vector(word) for word in words]

check_clusters_params = True
check_clusters_params = False
if check_clusters_params:
    test_vecs = vecs[:150]
    for eps in [0.1, 0.2, 0.3, 0.5, 0.7, 1, 1.5, 2, 3]:
        clusters = dbscan(eps=eps, n_jobs=-1, min_samples=3)
        clusters.fit(test_vecs)
        print('eps:', eps, clusters.labels_)

# print(words[0], vecs[0])
print('fit clusters')

compute_clusters = True
# compute_clusters = False
if compute_clusters:
    with open('lab3/data/fast_text_clusters.pkl', 'wb') as f:
        clusters = dbscan(eps=0.4, n_jobs=-1, min_samples=3)
        clusters.fit(vecs)
        joblib.dump(clusters, f)
else:
    with open('lab3/data/fast_text_clusters.pkl', 'rb') as f:
        clusters = joblib.load(f)

print(clusters.labels_[:200])
print('uniques:', Counter(clusters.labels_))
drop_clusters = True
# drop_clusters = False
if drop_clusters:
    print('drop clusters')

    with open('lab3/data/fast_text_data.json', 'w', encoding='utf-8') as f:
        data = {data[0]: int(data[1]) for data in zip(words, clusters.labels_)}
        json.dump(data, f, ensure_ascii=True)


