# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?envType=daily-question&envId=2024-04-08


from collections import deque
from typing import Counter, List

# hashmap approach
def countStudents(students: List[int], sandwiches: List[int]) -> int:
    res = len(students)
    count = Counter(students)

    for s in sandwiches:
        if count[s] > 0:
            res -= 1
            count[s] -= 1

        else:
            break
    
    return res

# simulation approach using a double-ended queue
def countStudents(students: List[int], sandwiches: List[int]) -> int:
    q = deque(students)
    i, count = 0, 0

    while len(q):
        curr = q.popleft()

        if curr != sandwiches[i]:
            count += 1
            q.append(curr)

        else:
            i += 1
            count = 0
        
        if count == len(q):
            break
    
    return len(q)


students = [1,1,0,0]
sandwiches = [0,1,0,1]

print(countStudents(students, sandwiches))