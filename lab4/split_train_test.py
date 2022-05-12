import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/Tweets.csv')

train, test = train_test_split(df, train_size=0.7, random_state=69)

print(train.head())

train.drop(['selected_text'], axis=1).to_csv('data/tweets_train.csv', index=False)
test.drop(['selected_text', 'sentiment'], axis=1).to_csv('data/tweets_test.csv', index=False)
test.drop(['text','selected_text'], axis=1).to_csv('data/submission_original.csv', index=False)
test['sentiment'] = 'neutral'
test.drop(['text','selected_text'], axis=1).to_csv('data/submission_sample.csv', index=False)
