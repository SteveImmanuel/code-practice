class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        self.generate_path(graph, 0, [], result)
        return result
    
    def generate_path(self, graph, current_node, traversal_list, result):
        traversal_list.append(current_node)
        
        if current_node == len(graph) - 1:
            result.append(traversal_list)
        else:
            traversal_list_len = len(traversal_list)
            for neighbor in graph[current_node]:
                traversal_list = traversal_list[:traversal_list_len]
                self.generate_path(graph, neighbor, traversal_list, result)