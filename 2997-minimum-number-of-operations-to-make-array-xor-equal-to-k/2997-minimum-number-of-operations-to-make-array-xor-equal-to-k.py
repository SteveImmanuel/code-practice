class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_bit = list(map(int, bin(k)[2:]))
        
        bit_count = defaultdict(int)
        for num in nums:
            bit_rep = list(map(int, bin(num)[2:]))
            for i in range(len(bit_rep) - 1, -1, -1):
                idx = len(bit_rep) - 1 - i
                # print(num, bit_rep, idx)
                if bit_rep[i] == 1:
                    bit_count[idx] += 1
        
        if len(bit_count) > 0:
            total_bits = max(bit_count.keys())
            # print(total_bits)
            all_xor = [None] * (total_bits + 1)
            # print(bit_count)
            for i in range(total_bits + 1):
                if bit_count[i] % 2 == 1:
                    all_xor[total_bits - i] = 1
                else:
                    all_xor[total_bits - i] = 0
        else:
            all_xor = []
        
        max_len = max(len(final_bit), len(all_xor))
        
        final_bit = [0] * (max_len - len(final_bit)) + final_bit
        all_xor = [0] * (max_len - len(all_xor)) + all_xor
        # print(final_bit)        
        total = 0
        for i in range(len(final_bit)):
            if final_bit[i] != all_xor[i]:
                total += 1
        return total
