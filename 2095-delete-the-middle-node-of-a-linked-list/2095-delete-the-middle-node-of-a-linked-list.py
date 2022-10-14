# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        prev = None
        
        while ptr2:
            ptr2 = ptr2.next
            if ptr2:
                ptr2 = ptr2.next
                prev = ptr1
                ptr1 = ptr1.next
                
        if prev:
            prev.next = ptr1.next
            return head
        return None
        