from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    # ensure both words contain the same set of characters
    if set(word1) != set(word2):
        return False

    # instead of sorting and counting frequencies, check that both words have the same count(frequency) for each character's frequency value
    return Counter(Counter(word1).values()) == Counter(Counter(word2).values())

word1, word2 = 'abc', 'bca'
print(closeStrings(word1, word2))