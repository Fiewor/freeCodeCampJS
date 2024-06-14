# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/?envType=daily-question&envId=2024-06-13

from typing import List

# using built-in sort
# time complexity -> O(nlogn)
# def minMovesToSeat(seats: List[int], students: List[int]) -> int:
#     res = 0
#     seats.sort()
#     students.sort()

#     for i in range(len(seats)):
#         res += abs(seats[i] - students[i])

#     return res


# using counting sort
def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    max_index = max(max(seats), max(students)) + 1
    count_seats = [0] * max_index
    count_students = [0] * max_index

    for i in range(len(seats)):
        count_seats[seats[i]] += 1
        count_students[students[i]] += 1

    res = 0
    i, j = 0, 0
    remain = len(students)

    while remain:
        if not count_seats[i]: 
            i += 1

        if not count_students[j]: 
            j += 1

        if count_seats[i] and count_students[j]:
            res += abs(i - j)
            count_seats[i] -= 1
            count_students[j] -= 1
            remain -= 1

    return res


seats = [4,1,5,9]
students = [1,3,2,6]
print(minMovesToSeat(seats, students))
