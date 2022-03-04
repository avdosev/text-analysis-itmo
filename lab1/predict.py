import json
import numpy as np

dict_path = "cache/data.json"


def lev_dist(fst, snd):
    f_size = len(fst) + 1
    s_size = len(snd) + 1

    matrix = np.zeros((f_size, s_size), int)
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


def main():
    test_word = input()
    key = ''.join(sorted(set(test_word)))
    with open(dict_path) as f:
        json_data = json.load(f)
        if key not in json_data:
            best_scores = dict()
            for key, val in json_data.items():
                score_word = dist_for_list(test_word, val)
                score, word = (min_score(score_word))
                best_scores[score] = word
            print(min_score(best_scores))
        else:
            score_word = dist_for_list(test_word, json_data[key])
            print(min_score(score_word))


if __name__ == "__main__":
    main()
