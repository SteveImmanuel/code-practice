# https://leetcode.com/problems/unique-binary-search-trees-ii/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return 'root=' + str(self.val)

class Solution:
    def copy_tree(self, ori_node:TreeNode, start_idx) -> TreeNode:
        if ori_node == None:
            return None

        print('copying', self.tree_to_arr(ori_node), 'startidx', start_idx)
        queue = []
        queue.append((ori_node, None))
        result = TreeNode(start_idx)
        cur_node = result

        while len(queue) > 0:
            visited_node, dir = queue.pop(0)
            if visited_node != None:
                # print('visitednode', visited_node)
                if dir == 'l':
                    cur_node.left = TreeNode(start_idx)
                    cur_node = cur_node.left
                else:
                    cur_node.right = TreeNode(start_idx)
                    cur_node = cur_node.right

                queue.append((visited_node.left, 'l'))
                queue.append((visited_node.right, 'r'))
                start_idx += 1
            # print(queue)

        print('res', self.tree_to_arr(result)) 
        return result

    def tree_to_arr(self, node) -> List:
        queue = []
        queue.append(node)
        res = []

        while len(queue) > 0:
            visited_node = queue.pop(0)
            # print('visitednode',visited_node)
            if visited_node == None:
                res.append(None)
            else:
                res.append(visited_node.val)
                queue.append(visited_node.left)
                queue.append(visited_node.right)
            # print('currentqueue',queue)
        
        while res[-1] == None:
            res.pop()

        return res

    def fix_value(self, node:TreeNode) -> List:
        idx = 1
        queue = []
        queue.append(node)

        while len(queue) > 0:
            visited_node = queue.pop(0)
            if visited_node != None:
                visited_node.val = idx
                queue.append(visited_node.left)
                queue.append(visited_node.right)
                idx += 1
            print(queue)
        print('node', self.tree_to_arr(node))

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memory = [[None]] * (n + 1)

        for i in range(1, n + 1):
            if i == 1:
                memory[i] = [TreeNode(1)]
            else:
                memory[i] = []
                for j in range(i):
                    left_nodes = j
                    right_nodes = (i - 1) - j
                    
                    for node_l in memory[left_nodes]:
                        for node_r in memory[right_nodes]:
                            c_node_l = self.copy_tree(node_l, 2)
                            c_node_r = self.copy_tree(node_r, 2 + left_nodes)
                            root = TreeNode(1, c_node_l, c_node_r)
                            memory[i].append(root)
        
        return memory[-1]

sol = Solution()
n = 3

# # tree = TreeNode(3, None, None)
# # tree.left = TreeNode(2, None, None)
# # tree.left.left = TreeNode(1, None, None)

# # tree = TreeNode(1, None, None)
# # tree.right = TreeNode(3, None, None)
# # tree.right.left = TreeNode(2, None, None)

# # tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))

# print(sol.tree_to_arr(tree))
print(sol.generateTrees(3))