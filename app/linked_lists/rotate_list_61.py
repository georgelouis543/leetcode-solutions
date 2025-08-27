# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # get the number of nodes
        n = 0
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next

        k = k % n
        if k == 0:
            return head

        # find the new tail (n-k-1 steps from head)
        curr = head
        for i in range(0, n - k - 1):
            curr = curr.next

        new_head = curr.next   # new head is after new tail
        curr.next = None       # cut the list

        # find the old tail
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head       # connect tail to old head

        return new_head