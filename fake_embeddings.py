word_vectors = {
    "car": [1, 0, 0],
    "automobile": [1, 0, 0],
    "vehicle": [1, 0, 0],

    "python": [0, 1, 0],
    "class": [0, 1, 0],
    "inheritance": [0, 1, 0],

    "apple": [0, 0, 1],
    "banana": [0, 0, 1]
}

def get_vector(word):
    if word in word_vectors:
        return word_vectors[word]
    return [0,0,0]

def similarity_vector(vec1, vec2):
    score = 0
    for i in range(len(vec1)):
        if vec1[i] == vec2[i]:
            score += 1
    return score

print(similarity_vector(get_vector("car"),get_vector("automobile")))