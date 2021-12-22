# Given the head of a singly linked list and two integers left and right
# where left <= right, reverse the nodes of the list
# from position left to position right, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head, m, n):
    p = dummy = ListNode(next=head)
    for _ in range(m - 1):
        p = p.next
    tail = p.next                   # tail=2->3->4->5
    for _ in range(n - m):          # dummy=0->1->2->3->4->5
        left = tail.next            # left=3->4->5      | 4->5
        tail.next = tail.next.next  # tail=2->4->5      | 2->5
        left.next = p.next          # left=3->2->4->5   | 4->3->2->5
        p.next = left               # p=1->3->2->4->5   | 1->4->3->2->5
    return dummy.next
