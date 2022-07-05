# https://leetcode.com/problems/odd-even-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        first_ptr = head
        second_ptr = head.next

        if second_ptr is None:
            return head

        second_head = head.next

        while first_ptr.next is not None and second_ptr.next is not None:
            first_ptr.next = first_ptr.next.next
            second_ptr.next = second_ptr.next.next
            
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        
        first_ptr.next = second_head
        return head

head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(7)
sol = Solution()
head = sol.oddEvenList(head)
while head != None:
    print(head.val)
    head = head.next