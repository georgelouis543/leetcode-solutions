# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        slow_ptr = 0

        fast = head
        fast_ptr = 0

        while fast and fast.next:
            slow = slow.next
            slow_ptr += 1

            fast = fast.next.next

            if slow is fast:
                slow = head

                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
