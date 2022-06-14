# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first_ptr = head

        length = 0
        while first_ptr is not None:
            length += 1
            first_ptr = first_ptr.next
        

        n_from_end = length - n
        first_ptr = head
        second_ptr = None
        
        if n_from_end == 0:
            return head.next

        i = 0
        while i < n_from_end:
            second_ptr = first_ptr
            first_ptr = first_ptr.next
            i += 1

        second_ptr.next = first_ptr.next
        return head        

sol = Solution()
arr = ListNode(1)
# arr.next = ListNode(2)
# arr.next.next = ListNode(3)
# arr.next.next.next = ListNode(4)
# arr.next.next.next.next = ListNode(5)
arr = sol.removeNthFromEnd(arr, 1)

print(arr.val, end='')
arr = arr.next
while arr is not None:
    print(',' + str(arr.val), end='')
    arr = arr.next
print()