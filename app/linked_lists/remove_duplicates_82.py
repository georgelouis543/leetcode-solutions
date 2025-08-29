# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        seen = set()

        while curr:
            if curr.next and curr.next.val == curr.val:
                seen.add(curr.val)
            curr = curr.next

        print(seen)

        dummy = head
        while dummy:
            if dummy.next and dummy.next.val in seen:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        if head and head.val in seen:
            head = head.next

        return head