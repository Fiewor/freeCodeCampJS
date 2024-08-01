# https://leetcode.com/problems/number-of-senior-citizens/description/?envType=daily-question&envId=2024-08-01

from typing import List

def countSeniors(details: List[str]) -> int:
    return sum([int(d[11:13]) > 60 for d in details])

def countSeniors(details: List[str]) -> int:
    re = 0
    for d in details:
        ten = ord(d[11]) - ord("0")
        one = ord(d[12]) - ord("0")
        age = ten*10 + one

        if age > 60:
            re += 1
    return re

print(countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"]))