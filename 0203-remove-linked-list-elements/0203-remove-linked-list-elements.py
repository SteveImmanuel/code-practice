# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        ohead = head
        ptr = head
        prev = None
        
        while ptr:
            while ptr and ptr.val == val:
                ptr = ptr.next
            
            if prev:
                prev.next = ptr
            
            prev = ptr
            if ptr:
                ptr = ptr.next
            
        return ohead
                
                
            