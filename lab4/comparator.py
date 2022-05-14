import pandas as pd

from sklearn.metrics import accuracy_score

import os
os.chdir('C:/projects/itmo/text-anal/')

def encode(df):
    return pd.DataFrame(
        {
            'sentiments_positive': (df == 'positive').astype(float),
            'sentiments_neutral': (df == 'neutral').astype(float),
            'sentiments_negative': (df == 'negative').astype(float),
        }
    )

def calculate_metrics(path):
    print('считаем для', path)
    y_true = encode(pd.read_csv('data/submission_original.csv')['sentiment'])
    y_predicted = encode(pd.read_csv(path)['sentiment'])

    print('accuracy:', accuracy_score(y_true, y_predicted))

    print('\n----\\\\----\n')

for item in sorted(os.listdir('data/submissions')):
    path = os.path.join('data/submissions', item)
    calculate_metrics(path)
