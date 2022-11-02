class Solution:
    def count_mutation(self, str1, str2):
        total = 0
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                total += 1
        return total
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        return self.traverse(start, end, bank)
    
    def traverse(self, current_gene, target_gene, untraversed_gene):
        if self.count_mutation(current_gene, target_gene) == 0:
            return 0
        else:
            min_mutation = -1
            for i in range(len(untraversed_gene)):
                if self.count_mutation(current_gene, untraversed_gene[i]) == 1:
                    next_mutation = self.traverse(untraversed_gene[i], target_gene, untraversed_gene[:i]+untraversed_gene[i+1:])
                    if next_mutation == -1:
                        continue
                        
                    current_mutation = 1 + next_mutation
                    if min_mutation == -1:
                        min_mutation = current_mutation
                    else:
                        min_mutation = min(min_mutation, current_mutation)
            return min_mutation
        
        
        