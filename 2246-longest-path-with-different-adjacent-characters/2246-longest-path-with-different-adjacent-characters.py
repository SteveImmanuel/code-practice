class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        child_dict = defaultdict(list)
        for i, p in enumerate(parent):
            child_dict[p].append(i)
        
        res = self.traverse(0, child_dict, s)
        return max(res[0], res[1])
            
    def traverse(self, cur_node, child_dict, s):
        if len(child_dict[cur_node]) == 0: # leaf
            # print(cur_node, [1, 0, s[cur_node]])
            return [1, 0, s[cur_node]]
        else:
            children_res = []
            for child in child_dict[cur_node]:
                children_res.append(self.traverse(child, child_dict, s))
            children_res.sort(key=lambda x: x[0], reverse=True)
            
            flattened_res = [(x[0], x[1]) for x in children_res]
            flattened_res = [x for y in flattened_res for x in y]
            
            top_two = []
            for child_res in children_res:
                if child_res[2] != s[cur_node]:
                    top_two.append(child_res)
                    if len(top_two) == 2:
                        break
            
            res = [1, max(flattened_res), s[cur_node]]
            if len(top_two) > 0:
                res[0] = 1 + top_two[0][0]
                if len(top_two) == 2:
                    res[1] = max(res[1], 1 + top_two[0][0] + top_two[1][0])
            # print(cur_node, res)
            return res
            
            