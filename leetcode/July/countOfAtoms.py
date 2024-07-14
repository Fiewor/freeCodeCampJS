# https://leetcode.com/problems/number-of-atoms/?envType=daily-question&envId=2024-07-14

from collections import defaultdict


def countOfAtoms(formula: str) -> str:
    stack = [defaultdict(int)]
    i = 0
    
    while i < len(formula):
        if formula[i] == "(":
            stack.append(defaultdict(int))

        elif formula[i] == ")":
            count = ""
            while i+1 < len(formula) and formula[i+1].isdigit():
                count += formula[i+1]
                i+=1
            count = 1 if not count else int(count)
            curr_map = stack.pop()
            prev_map = stack[-1]
            for elem in curr_map:
                prev_map[elem] += curr_map[elem] * count
                
        else:
            element = formula[i]
            if i+1 < len(formula) and formula[i+1].islower():
                element = formula[i:i+2]
                i+=1

            count = ""
            while i+1 < len(formula) and formula[i+1].isdigit():
                count += formula[i+1]
                i+=1
            count = 1 if not count else int(count)

            curr_map = stack[-1]
            curr_map[element] = count

        i += 1

    count_map = stack.pop()
    re = ""
    for elem in sorted(count_map.keys()):
        count = "" if count_map[elem] == 1 else count_map[elem]
        re += elem + str(count)

    return re

formula = "K4(ON(SO3)2)2"
print(countOfAtoms(formula)) # "K4N2O14S4"