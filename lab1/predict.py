import json
import numpy as np
import numba

dict_path = "lab1/cache/data.json"

@numba.njit()
def lev_dist(fst, snd):
    f_size = len(fst) + 1
    s_size = len(snd) + 1

    matrix = np.zeros((f_size, s_size))
    matrix[f_size - 1][s_size - 1] = 0
    for i in range(0, s_size):
        for j in range(0, f_size):
            if i == j == 0:
                matrix[i][j] = 0
            elif j == 0:
                matrix[j][i] = i
            elif i == 0:
                matrix[j][i] = j
            else:
                if fst[j - 1] == snd[i - 1]:
                    matrix[j][i] = matrix[j - 1][i - 1]
                else:
                    matrix[j][i] = min(matrix[j - 1][i - 1], matrix[j - 1][i], matrix[j][i - 1]) + 1
    return matrix[f_size - 1][s_size - 1]


def min_score(score_word):
    best_score = min(score_word.keys())
    return best_score, score_word[best_score]


def dist_for_list(test_word, words):
    dists = [lev_dist(test_word, word) for word in words]
    return dict(zip(dists, words))

def predict_words(test_word, json_data):
    key = ''.join(sorted(set(test_word)))
    char_set = set(test_word)
    char_set_len = len(char_set)
    best_scores = dict()
    for key, val in json_data.items():
        if char_set_len - len(set(key) & char_set) > 3:
            continue
        score_word = dist_for_list(test_word, val)
        score, word = min_score(score_word)
        if score not in best_scores:
            best_scores[score] = []
        best_scores[score].append(word)
    return best_scores

def main():
    print('load prepared data...')
    with open(dict_path) as f:
        json_data = json.load(f)
    print('loaded')
    while True:
        test_word = input('type word or q: ')
        if test_word == 'q':
            break
        
        variants = predict_words(test_word, json_data)
        variants = sorted(list(variants.items()), key=lambda x: x[0])
        for variant in variants[:2]:
            print(variant)
    


if __name__ == "__main__":
    main()
