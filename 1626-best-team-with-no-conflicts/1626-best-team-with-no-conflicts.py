class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pair = [(age, score) for age, score in zip(ages, scores)]
        pair.sort(key=lambda x: (x[0], x[1]))
        mem = [None] * len(pair)
        
        for i in range(len(mem)):
            cur_score = pair[i][1]
            max_additional = 0
            for j in range(i):
                if pair[i][1] >= pair[j][1] and mem[j] > max_additional:
                    max_additional = mem[j]
            mem[i] = cur_score + max_additional
        # print(mem)
        
        
        
        return max(mem)
        