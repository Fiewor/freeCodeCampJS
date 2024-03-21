# https://leetcode.com/problems/reverse-linked-list/?envType=daily-question&envId=2024-03-21

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# iterative
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = next = None
    
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

# recursive
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None: 
        return head
    res = reverseList(head.next)
    head.next.next = head
    head.next = None
    return res

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))   
print(reverseList(head))