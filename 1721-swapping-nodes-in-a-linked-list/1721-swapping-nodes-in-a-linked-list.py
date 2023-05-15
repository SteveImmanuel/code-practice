# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        
        norm_k = k
        if k > length / 2:
            norm_k = length - k + 1
        
        ptr = head
        cur_k = 1
        
        while ptr and cur_k < norm_k:
            ptr = ptr.next
            cur_k += 1
            
        node_f = ptr
        
        ptr = head
        ptr2 = node_f
        
        while ptr2.next:
            ptr = ptr.next            
            ptr2 = ptr2.next
        
        node_r = ptr
        node_f.val, node_r.val = node_r.val, node_f.val
        
        return head
