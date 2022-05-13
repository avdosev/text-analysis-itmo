from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

test_csv = pd.read_csv('data/tweets_test.csv')
train_csv = pd.read_csv('data/tweets_train.csv')

train_X = train_csv['text']
train_y = train_csv['sentiment']

test_id = test_csv['textID']
test_X = test_csv['text']

tf_vectorizer = TfidfVectorizer(use_idf=True)

X_train_tf = tf_vectorizer.fit_transform(train_X)

X_test_tf = tf_vectorizer.transform(test_X.values.astype('U'))

naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(X_train_tf, train_y)

y_pred = naive_bayes_classifier.predict(X_test_tf)

csv_dict = {'textID': test_id, 'sentiment': y_pred}
csv_df = pd.DataFrame(csv_dict)
csv_df.to_csv('data/my_submission.csv', sep=',', encoding='utf-8', index=False)
