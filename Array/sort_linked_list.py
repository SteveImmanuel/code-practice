# https://leetcode.com/problems/sort-list/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head
        # while temp is not None:
        #     print(temp.val)
        #     temp = temp.next
        # print()
        if head is None or head.next is None:
            return head

        ptr1 = head
        ptr2 = head

        while ptr2 is not None:
            ptr2 = ptr2.next
            if ptr2 is not None:
                ptr2 = ptr2.next
                if ptr2 is not None:
                    ptr1 = ptr1.next
        
        head2 = ptr1.next
        ptr1.next = None
        # print(ptr1.val, ptr1.next)

        # print(head.val)
        # print(head2.val)
        head1 = self.sortList(head)
        head2 = self.sortList(head2)

        sorted_head = self.merge(head1, head2)
        return sorted_head

    def merge(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        ptr1 = head1
        ptr2 = head2
        if head1.val < head2.val:
            new_head = head1
            ptr1 = ptr1.next
        else:
            new_head = head2
            ptr2 = ptr2.next

        main_ptr = new_head

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val < ptr2.val:
                main_ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                main_ptr.next = ptr2
                ptr2 = ptr2.next
            main_ptr = main_ptr.next
        
        if ptr1 is not None:
            main_ptr.next = ptr1
        elif ptr2 is not None:
            main_ptr.next = ptr2
        
        return new_head
        

sol = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(9)
new_head = sol.sortList(head)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next