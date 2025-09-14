# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        hash_set = set(nums)

        while curr and curr.next:
            if curr.next.val in hash_set:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
