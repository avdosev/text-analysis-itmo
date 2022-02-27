import json
import os

data_path = 'data/out/AA'

texts = []

for file_name in os.listdir(data_path):
    print('preparing: {}'.format(file_name))
    with open(os.path.join(data_path,file_name)) as f:
        lines = f.readlines()
        for line in lines:
            text = json.loads(line)['text']
            texts.append(text)

# todo: 
# подготовить тексты 
# разбить на слова 
# сделать предвычисления
# сохранить в папку lab1/cahce

