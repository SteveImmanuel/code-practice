class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        mem = {}
        visited = set()
        result = []
        for i in range(len(graph)):
            self.traverse(i, graph, visited, mem)
            if mem[i]:
                result.append(i)
        return result
        
    def traverse(self, cur_node, graph, visited, mem):
        if cur_node not in mem:
            if cur_node in visited:
                return
                
            visited.add(cur_node)
            if len(graph[cur_node]) == 0:
                mem[cur_node] = True
            else:
                
                is_safe = True
                for node in graph[cur_node]:
                    is_safe = is_safe and self.traverse(node, graph, visited, mem)
                mem[cur_node] = is_safe
                
        
        return mem[cur_node]