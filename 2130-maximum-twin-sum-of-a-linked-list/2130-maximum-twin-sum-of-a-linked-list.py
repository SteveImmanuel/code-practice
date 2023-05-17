# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        
        front = head
        back = head
        
        i = 0
        while i < length // 2:
            i += 1
            back = back.next
        
        back_next = back.next
        first = True
        while back_next:
            temp_next = back_next.next
            back_next.next = back
            if first:
                first = False
                back.next = None
            back = back_next
            back_next = temp_next
        
        max_sum = 0
        while back and front:
            max_sum = max(max_sum, back.val + front.val)
            back = back.next
            front = front.next
        
        return max_sum