# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashSet = set()
        curr = head

        while curr is not None:
            if curr.next in hashSet:
                return True
            hashSet.add(curr)
            curr = curr.next

        print(hashSet)

        return False
