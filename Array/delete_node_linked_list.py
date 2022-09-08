# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ptr = node
        ptr.val = ptr.next.val
        ptr.next = ptr.next.next

node = ListNode(4)
node.next = ListNode(5)
node.next.next = ListNode(1)
node.next.next.next = ListNode(9)
sol = Solution()
sol.deleteNode(node.next)

while node is not None:
    print(node.val)
    node = node.next