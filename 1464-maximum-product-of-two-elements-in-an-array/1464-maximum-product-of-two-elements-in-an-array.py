class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg_nums = list(map(lambda x:-x, nums))
        heapq.heapify(neg_nums)
        num1 = -heapq.heappop(neg_nums)
        num2 = -heapq.heappop(neg_nums)
        return (num1-1) * (num2-1)