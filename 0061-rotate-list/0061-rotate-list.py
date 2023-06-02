# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        if length <= 1 or k == 0:
            return head
        head_idx = (length - (k % length)) % length
        if head_idx == 0:
            return head
        
        ptr = head
        prev = None
        cur_idx = 0
        while cur_idx != head_idx:
            prev = ptr
            ptr = ptr.next
            cur_idx += 1
        
        new_head = ptr
        prev.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        return new_head