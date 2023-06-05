# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        if head.next.val != head.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            val = head.val
            while head and head.val == val:
                head = head.next
            if head:
                return self.deleteDuplicates(head)
            return None
            
        
            