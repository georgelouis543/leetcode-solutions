# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    dummy = head
    n = 0
    while dummy:
        n += 1
        dummy = dummy.next

    print(n)
    print(k)

    if n == k:
        head.value = head.next.value
        head.next = head.next.next
        return head

    curr = head
    for i in range(0, n - k - 1):
        curr = curr.next

    # print(curr.value)
    temp = curr
    temp2 = curr.next.next
    # print(temp2.value)

    temp.next = temp2

    return head
