class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        edge_dict = defaultdict(list)
        for node1, node2 in edges:
            edge_dict[node1].append(node2)
            edge_dict[node2].append(node1)
        
        ans = [None for _ in range(n)]
        self.traverse(0, edge_dict, labels, set(), ans)
        return ans
    
            
    def combine_dicts(self, dicts):
        res = Counter()
        for c in 'abcdefghijklmnopqrstuvwxyz':
            for d in dicts:
                res[c] += d[c]
        return res
            
        
    def traverse(self, cur_node, edge_dict, labels, visited, answer_arr):
        if cur_node in visited:
            return Counter()
        
        visited.add(cur_node)
        if len(edge_dict[cur_node]) == 1 and cur_node != 0:
            answer_arr[cur_node] = 1
            res = Counter()
            res[labels[cur_node]] = 1
            # print(cur_node, res, visited)
            return res
        else:
            dicts = []
            for child in edge_dict[cur_node]:
                dicts.append(self.traverse(child, edge_dict, labels, visited, answer_arr))
            res = self.combine_dicts(dicts)
            res[labels[cur_node]] += 1
            # print(cur_node, res, visited)
            answer_arr[cur_node] = res[labels[cur_node]]
            return res
            
            