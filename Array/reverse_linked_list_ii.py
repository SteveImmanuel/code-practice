# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def create_linked_list(self, arr):
        if len(arr) == 0:
            return None
        
        head = ListNode(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = ListNode(arr[i])
            tail = tail.next
        return head, tail
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr_1 = head
        ptr_2 = None
        i = 1

        while i < left:
            ptr_2 = ptr_1
            ptr_1 = ptr_1.next
            i += 1

        left_el = ptr_1

        while i < right:
            ptr_1 = ptr_1.next
            i += 1

        arr = []
        right_el = ptr_1
        while left_el != right_el:
            arr.append(left_el.val)
            left_el = left_el.next
        arr.append(right_el.val)
        arr = arr[::-1]
        arr_head, arr_tail = self.create_linked_list(arr)

        if ptr_2 is None:
            head = arr_head
        else:
            ptr_2.next = arr_head

        arr_tail.next = right_el.next
        return head


sol = Solution()
head,_ = sol.create_linked_list([1,2,3,4,5,6,7,8,9])    
head = sol.reverseBetween(head, 1, 3)
while head is not None:
    print(head.val)
    head = head.next
