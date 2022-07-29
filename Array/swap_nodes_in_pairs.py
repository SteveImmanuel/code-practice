# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        front_ptr = head
        first = True

        while front_ptr is not None:
            if not first:
                prev_nodes = prev_nodes.next.next

            back_ptr = front_ptr.next

            if back_ptr is not None:
                front_ptr.next = back_ptr.next
                back_ptr.next = front_ptr
                if first:
                    first = False
                    head = back_ptr
                    prev_nodes = ListNode(0, head)
                else:
                    prev_nodes.next = back_ptr

            front_ptr = front_ptr.next

        return head

head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

sol = Solution()
head = sol.swapPairs(head)

while head is not None:
    print(head.val)
    head = head.next