class Node:
    def __init__(self, val, children, is_file):
        self.val = val
        self.children = children
        self.len = len(val)
        self.is_file = is_file
        
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = 'tmp\n' + input
        tree = self.parse(input, 0)
        # print(tree.children)
        # for x in tree.children:
        #     print(x.val, x.len)
        # print(tree.children[1].children)
        # print(tree.children[1].children[0].val, tree.children[1].children[0].len)
        return max(self.get_max_len(tree, 0) - 4, 0)
    
    def get_max_len(self, root, cur_len):
        # print(root.val, root.len, cur_len)
        
        if len(root.children) == 0:
            if root.is_file == True:
                return cur_len + root.len
            else:
                return 0
        max_len = 0
        for child in root.children:
            max_len = max(max_len, self.get_max_len(child, cur_len + root.len + 1))
        return max_len
        
        
        
    def parse(self, input, cur_depth=1):
        sep = '\n' + '\t' * cur_depth
        res = input.split(sep)
        i = 0
        while i < len(res):
            if res[i][0] != '\t':
                if i + 1 >= len(res) or res[i+1][0] != '\t':
                    i += 1
                else:
                    res[i] += sep + res[i+1]
                    res.pop(i+1)
        
        children = []
        for i in range(1, len(res)):
            children.append(self.parse(res[i], cur_depth+1))
        is_file = len(children) == 0 and '.' in res[0]
        return Node(res[0], children, is_file)
    
        