class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [set(), defaultdict(int)]
        loser_set = set()
        
        for winner, losser in matches:
            answer[0].add(winner)
            answer[1][losser] += 1
            loser_set.add(losser)
        
        answer[0] = list(answer[0].difference(loser_set))
        answer[1] = [loser for loser, count in answer[1].items() if count == 1]
        
        answer[0].sort()
        answer[1].sort()
        return answer
            
            