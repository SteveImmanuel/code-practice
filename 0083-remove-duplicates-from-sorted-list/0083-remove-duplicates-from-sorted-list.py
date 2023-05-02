# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ori = head
        anchor = head
        ptr = head
        
        while ptr:
            while ptr and anchor.val == ptr.val:
                ptr = ptr.next

            anchor.next = ptr
            anchor = ptr
        
        return ori
