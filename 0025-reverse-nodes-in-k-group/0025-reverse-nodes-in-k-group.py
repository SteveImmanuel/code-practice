# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.len(head)
        total_groups = length // k
        
        last_tail = None
        ptr = head
        new_head = head
        # print(length, k, total_groups)
        for i in range(total_groups):
            cur_head, last_tail = self.reverse_node(ptr, last_tail, k)
            if i == 0:
                new_head = cur_head
            ptr = last_tail.next
        
        return new_head
        
    def len(self, head):
        i = 0
        ptr = head
        while ptr:
            i += 1
            ptr = ptr.next
        return i
        
    def reverse_node(self, head, last_tail, k):
        # print(head.val, last_tail.val if last_tail else None)
        tail = head
        cur_ptr = head
        prev_ptr = None
        
        i = 0
        while cur_ptr and cur_ptr.next and i < k:
            # print(cur_ptr.val)
            next_ptr = cur_ptr.next
            cur_ptr.next = prev_ptr
            prev_ptr = cur_ptr
            cur_ptr = next_ptr
            i += 1
            
        if i < k and cur_ptr:
            # print(cur_ptr.val, prev_ptr.val, i)
            cur_ptr.next = prev_ptr
            prev_ptr = cur_ptr
            cur_ptr = None
        
        tail.next = cur_ptr
        if last_tail:
            last_tail.next = prev_ptr
        # print(' ', prev_ptr.val, tail.val)
        return prev_ptr, tail