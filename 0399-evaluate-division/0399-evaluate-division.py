class Solution:
    def calculate(self, var1, var2, calculation_dict, visited):
        if var2 not in calculation_dict[var1]:
            visited.add(var1)
            found = False
            for inter_var in calculation_dict[var1]:
                if inter_var in visited or calculation_dict[var1][inter_var] == -1:
                    continue
                    
                res = self.calculate(inter_var, var2, calculation_dict, visited)
                if res != -1:
                    found = True
                    calculation_dict[var1][var2] = res * calculation_dict[var1][inter_var]
                    calculation_dict[var2][var1] = 1 / calculation_dict[var1][var2]
                    break
                    
            if not found:
                calculation_dict[var1][var2] = -1
                calculation_dict[var2][var1] = -1
                
        return calculation_dict[var1][var2]
                    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        calculation_dict = defaultdict(dict)
        for (var1, var2), val in zip(equations, values):
            calculation_dict[var1][var2] = val
            calculation_dict[var2][var1] = 1 / val
            
        res = []
        for query in queries:
            res.append(self.calculate(query[0], query[1], calculation_dict, set()))
            print(query, calculation_dict)
            print()
            
        
        return res