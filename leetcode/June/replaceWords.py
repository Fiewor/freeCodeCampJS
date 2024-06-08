from typing import List

# set solution
def replaceWords(dictionary: List[str], sentence: str) -> str:
    roots = set(dictionary)
    res = []

    for word in sentence.split():
        for i in range(len(word) + 1):
            if word[:i] in roots:
                res.append(word[:i])
                break
        else: res.append(word)

    return ' '.join(res)

# trie solution
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
    
    def startsWith(self, word):
        node = self.root
        prefix = ''
        for char in word:
            if char not in node.children:
                return word
            prefix += char
            if node.children[char].isEndOfWord:
                return prefix
            node = node.children[char]
        return word # doesn't matter at this point if you return the prefix you've built so far or the original word

def replaceWords(dictionary: List[str], sentence: str) -> str:
    trie = Trie()
    res = []

    for word in dictionary:
        trie.insert(word)
    
    for word in sentence.split():
        res.append(trie.startsWith(word))

    return ' '.join(res)


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dictionary, sentence))

