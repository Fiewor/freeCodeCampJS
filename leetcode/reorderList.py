# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    rightStart = slow
    # reverse right
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
    first_half = head
    second_half = prev

    while second_half.next:
        temp = first_half.next
        first_half.next = second_half
        first_half = temp

        temp2 = second_half.next
        second_half.next = first_half
        second_half = temp2


#! correct, but probably less-readable version 
def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = fast = head

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    prev = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next

    first_half = head
    second_half = prev

    while second_half.next:
        first_half.next, first_half = second_half, first_half.next
        second_half.next, second_half = first_half, second_half.next



