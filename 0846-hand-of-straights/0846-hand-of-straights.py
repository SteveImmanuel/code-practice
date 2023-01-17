class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        sorted_hand = sorted(hand)
        occ = Counter(sorted_hand)

        smallest_idx = 0
        while len(occ) > 0:
            current_smallest = sorted_hand[smallest_idx]
            min_occ = occ.pop(current_smallest)
            
            for i in range(current_smallest + 1, current_smallest + groupSize):
                if occ[i] >= min_occ:
                    occ[i] -= min_occ
                    if occ[i] == 0:
                        occ.pop(i)
                else:
                    return False
            
            while smallest_idx < len(sorted_hand) and sorted_hand[smallest_idx] not in occ:
                smallest_idx += 1
        
        return True