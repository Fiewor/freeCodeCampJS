# https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    count = 0
    prev = None
    first = list1
    
    while list1 and count < a:
        prev = list1
        count += 1
        list1 = list1.next
    
    if prev:
        prev.next = list2
    else:
        first = list2
    
    while list2 and list2.next:
        list2 = list2.next

    while list1 and count < b:
        count += 1
        list1 = list1.next
    
    if list2:
        list2.next = list1.next

    return first


def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    curr = list1
    count = 0

    while count < a - 1:
        count += 1
        curr = curr.next

    head = curr
    while count <= b:
        count += 1
        curr = curr.next
    
    head.next = list2
    
    while list2.next:
        list2 = list2.next
    
    list2.next = curr

    return list1


list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
list2 = ListNode(1000, ListNode(1001, ListNode(1002)))
a = 3
b = 4
print(mergeInBetween(list1, a, b, list2))