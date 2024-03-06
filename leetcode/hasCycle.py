# https://leetcode.com/problems/linked-list-cycle/?envType=daily-question&envId=2024-03-06


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

listnode1 = ListNode(3)
listnode2 = ListNode(2)
listnode1.next = listnode2
listnode3 = ListNode(0)
listnode2.next = listnode3
listnode4 = ListNode(-4)
listnode4.next = listnode2
listnode3.next = listnode4

print(hasCycle(listnode1))