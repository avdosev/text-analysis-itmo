import json
import random

n_grams_dir = 'cache/data.json'


def continue_anek(key_word, n_grams):
    relevant_n_grams = []
    for key, val in n_grams.items():
        words = key.split('~')
        if words[0] == key_word:
            relevant_n_grams.append((key, val))

    part_sum = []
    for key, val in relevant_n_grams:
        part_sum.append(val if len(part_sum) == 0 else part_sum[-1] + val)

    probability = random.random()
    min_dist = 1.0
    most_relevant_id = -1
    for i in range(len(part_sum)):
        if abs(part_sum[i] - probability) < min_dist:
            min_dist = abs(part_sum[i] - probability)
            most_relevant_id = i
    res = relevant_n_grams[most_relevant_id][0].split('~')[1:]
    return res


def main():
    key_word = input('Enter anek key_word: ')

    print('load prepared data...')
    with open(n_grams_dir) as f:
        n_grams = json.load(f)

    anek = []
    anek.extend(key_word.split(' '))
    end_seq_cnt = 0
    while end_seq_cnt < 2:
        result = continue_anek(anek[-1].lower(), n_grams)
        if result[-1] == '__end_seq':
            result[-1] = '.'
            end_seq_cnt += 1
        if len(anek) % 30 == 0:
            anek.append('\n')
        anek.extend(result)

    print(' '.join(anek))


if __name__ == "__main__":
    main()
