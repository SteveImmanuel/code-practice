# https://leetcode.com/problems/partition-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = None
        head2 = None
        main_ptr = head
        ptr1 = None
        ptr2 = None

        while main_ptr is not None:
            if main_ptr.val < x:
                if head1 is None:
                    head1 = main_ptr
                    ptr1 = head1
                else:
                    ptr1.next = main_ptr
                    ptr1 = ptr1.next

            else:
                if head2 is None:
                    head2 = main_ptr
                    ptr2 = head2
                else:
                    ptr2.next = main_ptr
                    ptr2 = ptr2.next

            main_ptr = main_ptr.next

        if ptr2 is not None:
            ptr2.next = None

        if ptr1 is None:
            return head2
        
        ptr1.next = head2
        return head1





head = ListNode(1)
# head.next = ListNode(4)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(2)

sol = Solution()
head = sol.partition(head, 0)
while head != None:
    print(head.val)
    head = head.next