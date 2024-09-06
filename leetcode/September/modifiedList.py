# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2024-09-06

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

def modifiedList(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set(nums)
    dummy = ListNode(0, head)
    prev = dummy
    cur = head # or dummy.next

    while cur:
        if cur.val in nums:
            prev.next = cur.next
        else:
            prev = prev.next
        cur = cur.next
    
    return dummy.head