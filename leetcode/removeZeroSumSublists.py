# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    prefix_sum = 0
    dummy = ListNode(0)
    dummy.next = head
    map = {prefix_sum: dummy}

    while head:
        prefix_sum += head.val

        if prefix_sum in map:
            node_to_remove = map[prefix_sum].next
            SUM = prefix_sum

            while node_to_remove != head:
                SUM += node_to_remove.val
                del map[SUM]
                node_to_remove = node_to_remove.next

            map[prefix_sum].next = head.next
        else:
            map[prefix_sum] = head

        head = head.next

    return dummy.next

# test case
listnode = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
res = removeZeroSumSublists(listnode)
arr = []
while res:
    arr.append(res.val)
    res = res.next
print(arr)