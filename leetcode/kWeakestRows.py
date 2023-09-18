# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/?envType=daily-question&envId=2023-09-18
import heapq

def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
# ----------- sorting ------------
#     row_strength = {}
#     for i in range(len(mat)):
#         row_strength[i] = sum(mat[i])
#     sorted_rows = sorted(row_strength.items(), key=lambda x: x[1])
#     return [indx for indx, _ in sorted_rows[:k]]


# ----------- heap ------------
    # heap = []

    # for i, row in enumerate(mat):
    #     strength = sum(row)

    #     heappush(heap, (-strength, -i))

    #     if len(heap) > k:
    #         heappop(heap)
    
    # return [-ind for _, ind in sorted(heap, reverse=True)]


# ---------- binary search and heap ----------
    def binarySearch(arr):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

    st = [(binarySearch(row), i) for i, row in enumerate(mat)]

    heapq.heapify(st)

    return [i for _, i in heapq.nsmallest(k, st)]