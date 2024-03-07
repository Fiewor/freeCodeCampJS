# https://leetcode.com/problems/middle-of-the-linked-list/?envType=daily-question&envId=2024-03-07 

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# counter approach
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    count = 1
    copy = head

    if head.next == None:
        return head

    while copy.next:
        count += 1
        copy = copy.next
    
    currCount = 1
    while head.next:
        head = head.next
        if currCount == count // 2:
            return head
        currCount += 1

# tortoise and hare aapproach
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

listnode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(middleNode(listnode))