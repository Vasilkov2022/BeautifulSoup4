import json
import re
from string import punctuation

with open("vacancies.json") as file:
    lines = json.loads(file.read())
    # print(lines.values())
    lines = list(lines.values())




def get_words(line: str):
    line = line.lower()
    line = re.sub(f'[{punctuation}]', '', line)

    return line.split()

def get_matrix():
    # print([i for i in lines.values()])
    texts = list(map(get_words, [i['description'] for i in lines[0]]))
    # print(texts)
    unigue_words = sum(texts, [])
    dict_words = {key: i for i, key in enumerate(unigue_words)}
    matrix = []

    for text in texts:
        vec = [0] * len(unigue_words)
        for word in text:
            index = dict_words[word]
            vec[index] += 1
        matrix.append(vec)

    return matrix


def hamming_distance(vec1, vec2):
    distance = 0
    for i in range(len(vec1)):
        if vec1[i] ^ vec2[i]:
            distance += 1
    return distance


def compare_text():
    matrix = get_matrix()
    dict_distances = dict()

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > j:
                dict_distances[(i, j)] = hamming_distance(matrix[i], matrix[j])
    max_value = max(dict_distances.values())
    for i in dict_distances.keys():
        dict_distances[i] /= max_value

    srt = (sorted([(k, v) for k, v in dict_distances.items()], key=lambda x: x[1]))
    # print(srt)

    ids = []
    for i in srt:
        id = i[0]
        ids.append(id)
    # print(ids)


    for id in range(5):
        print(' '.join(names(ids[id][0], ids[id][1])))
        print()



    # return hamming_distance(matrix[1], matrix[2])

def names(a, b):
    orgs = []
    texts = list(map(get_words, [i['name'] for i in lines[0]]))
    for nam in texts:
        name = (' '.join(nam))
        orgs.append(name)
    return orgs[a], "and", orgs[b]



compare_text()


