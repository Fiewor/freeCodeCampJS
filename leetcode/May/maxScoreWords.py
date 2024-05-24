# https://leetcode.com/problems/maximum-score-words-formed-by-letters/?envType=daily-question&envId=2024-05-24

from collections import Counter
from typing import List

def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
    letter_count = Counter(letters)

    def can_form_word(word, count):
        word_count = Counter(word)
        for char in word:
            if word_count[char] > count[char]:
                return False
        return True
    
    def get_score(word):
        res = 0
        for char in word:
            res += score[ord(char) - ord('a')]
        return res

    def backtrack(i):
        if i == len(words):
            return 0
        
        res = backtrack(i+1) #skip
        if can_form_word(words[i], letter_count):
            for char in words[i]:
                letter_count[char] -= 1

                res =  max(res, get_score(words[i]) + backtrack(i+1)) #include

            for char in words[i]:
                letter_count[char] += 1
        return res

    return backtrack(0)

words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

print(maxScoreWords(words, letters, score))