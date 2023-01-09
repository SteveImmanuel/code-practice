class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        counter_s2 = Counter(s2[:len(s1)])
        
        for key in set(counter_s1).union(counter_s2):
            if key in counter_s2:
                counter_s2[key] -= counter_s1[key]
            elif key not in counter_s2 and key in counter_s1:
                counter_s2[key] -= counter_s1[key]
                
            if counter_s2[key] == 0:
                del counter_s2[key]
        
        if len(counter_s2) == 0:
            return True
        
        end = len(s1)
        while end < len(s2):
            start = end - len(s1)
            
            counter_s2[s2[end]] += 1
            if counter_s2[s2[end]] == 0:
                del counter_s2[s2[end]]
            
            counter_s2[s2[start]] -= 1
            if counter_s2[s2[start]] == 0:
                del counter_s2[s2[start]]
            
            if len(counter_s2) == 0:
                return True
            # print(end, counter_s2)
                        
            end += 1
            
            
        return False
                
                
            