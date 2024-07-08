class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nodes = []
        for i in range(1, n+1):
            nodes.append(Node(i))
        for i in range(n):
            nodes[i].next = nodes[(i+1) % n]
        cur = nodes[0]
        prev = nodes[-1]
        for _ in range(n):
            for _ in range(k - 1):
                cur = cur.next
                prev = prev.next
            cur = cur.next
            prev.next = cur
        return cur.val
            