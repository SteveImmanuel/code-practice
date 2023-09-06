# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_len = self.length(head)
        div, mod = divmod(list_len, k)
        
        result = []
        global_ptr = head
        for i in range(k):
            total_len = div + (1 if i < mod else 0)

            cur_head = None
            cur_ptr = None
            cur_len = 0
            while cur_len < total_len:
                if cur_len == 0:
                    cur_head = global_ptr
                    cur_ptr = global_ptr
                else:
                    cur_ptr = cur_ptr.next
                    global_ptr = global_ptr.next
                cur_len += 1
            
            if global_ptr is not None:
                global_ptr = global_ptr.next
            if cur_ptr is not None:
                cur_ptr.next = None
            result.append(cur_head)
        
        return result
    
    
    def length(self, head):
        length = 0
        ptr = head
        while ptr is not None:
            length += 1
            ptr = ptr.next
        return length