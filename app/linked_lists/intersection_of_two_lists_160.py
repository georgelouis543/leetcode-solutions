# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB

        while A != B:
            if A is not None:
                A = A.next
            else:
                A = headB

            if B is not None:
                B = B.next
            else:
                B = headA

        return B