class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        num_dict = defaultdict(int)
        num_bits = len(matrix[0])
        mask = (1 << num_bits) - 1
        for x in matrix:
            num = '0b' + ''.join(map(str, x))
            num = int(num, 2)
            
            key = num
            if key not in num_dict:
                key = key ^ mask
            num_dict[key] += 1
        # print(num_dict)
        return max(num_dict.values())