def replaceWords(dictionary, sentence):
    roots = set(dictionary)
    res = []

    for word in sentence.split():
        for i in range(len(word) + 1):
            if word[:i] in roots:
                res.append(word[:i])
                break
        else: res.append(word)

    return ' '.join(res)

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dictionary, sentence))