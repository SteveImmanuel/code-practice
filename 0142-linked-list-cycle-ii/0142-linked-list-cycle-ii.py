class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle = head
        hare = head
        first = True
        while hare and hare.next and (first or hare != turtle):
            first = False
            hare = hare.next
            if hare:
                hare = hare.next
            turtle = turtle.next
        #print(hare.val, turtle.val)
        if hare != turtle or first:
            return None
        
        turtle = head
        while turtle != hare:
            turtle = turtle.next
            hare = hare.next

        return turtle