class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        pair_dict = defaultdict(list)
        for i in range(1, len(adjacentPairs)):
            pair_dict[adjacentPairs[i][0]].append(adjacentPairs[i][1])
            pair_dict[adjacentPairs[i][1]].append(adjacentPairs[i][0])
            
        head = ListNode(adjacentPairs[0][0])
        tail = ListNode(adjacentPairs[0][1])
        head.next = tail
        
        processed = set()
        while len(processed) != len(adjacentPairs) + 1:
            last_head = head
            last_tail = tail
            
            for x in pair_dict[last_head.val]:
                if x not in processed:
                    head = ListNode(x, last_head)
            processed.add(last_head.val)
            
            for x in pair_dict[last_tail.val]:
                if x not in processed:
                    tail.next = ListNode(x)
                    tail = tail.next
            processed.add(last_tail.val)
            
            # print(processed)
        # print(head.val, tail.val)
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
            
            
                    
            
        