# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from typing import List


def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}

        for i in range(len(matches)):
            losses[matches[i][0]] = 0
            losses[matches[i][1]] = 0

        for i in range(len(matches)):
            if matches[i][1] in losses:
                losses[matches[i][1]] += 1
                
        return [sorted([i for i in losses if losses[i] == 0]), sorted([i for i in losses if losses[i] == 1])]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches))