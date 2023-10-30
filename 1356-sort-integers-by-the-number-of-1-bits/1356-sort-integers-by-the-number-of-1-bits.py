class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        new_arr = [(self.count_ones(x), x) for x in arr]
        new_arr.sort()
        return list(map(lambda x:x[1], new_arr))
    
    def count_ones(self, num):
        num_bin = bin(num)[2:]
        return Counter(list(num_bin))['1']