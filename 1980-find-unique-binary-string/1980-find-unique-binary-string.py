class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums[0])
        l = 0
        r = (2 ** n)
        num_set = set([int(x, 2) for x in nums])
        for i in range(l, r):
            if i not in num_set:
                return bin(i)[2:].zfill(n)