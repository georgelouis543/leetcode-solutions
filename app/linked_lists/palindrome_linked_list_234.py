# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        nums = []

        while curr:
            nums.append(curr.val)
            curr = curr.next

        print(nums)

        if nums[::-1] == nums:
            return True

        return False
