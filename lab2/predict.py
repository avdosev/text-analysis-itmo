from base64 import encode
import json
import random

def continue_anek(key, n_grams):
    relevant = n_grams[key]
    part_sum = []
    for key, val in relevant:
        part_sum.append(val if len(part_sum) == 0 else part_sum[-1] + val)

    probability = random.random()
    min_dist = 1.0
    most_relevant_id = -1
    for i in range(len(part_sum)):
        if abs(part_sum[i] - probability) < min_dist:
            min_dist = abs(part_sum[i] - probability)
            most_relevant_id = i
    res = relevant[most_relevant_id][0].split('~')[n-1:]
    return res

def prepare_relevant(n_grams):
    result = {}
    for key, val in n_grams.items():
        i = key.rfind('~')
        words = [key[:i], key[i+1:]]
        key_word = words[0]
        if key_word not in result:
            result[key_word] = []
        result[key_word].append((key, val))
    return result
    

def main():
    global n
    n = int(input('type n_grams count: '))
    print('load prepared data...')
    n_grams_dir = f'lab2/cache/data_{n}.json'
    with open(n_grams_dir, encoding='utf-8') as f:
        n_grams = json.load(f)

    n_grams = prepare_relevant(n_grams)
    
    while True:
        key_word = input('Enter anek key_word: ')
        if key_word == 'exit': break

        anek = []
        anek.extend(key_word.split(' '))
        
        while True:
            key = '~'.join(word.lower() for word in anek[-n+1:])
            # print(key)
            result = continue_anek(key, n_grams)
            # print(result)
            if result[-1] == '__end_seq':
                break
            anek.extend(result)

        print(' '.join(anek))


if __name__ == "__main__":
    main()
