# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        total_nodes = 0
        while curr:
            total_nodes += 1
            curr = curr.next

        print(total_nodes)
        mid = total_nodes // 2
        print(mid)

        if mid == 0:
            return None

        curr = head
        i = 0
        while i < mid:
            if i == mid - 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
            i += 1

        return head
