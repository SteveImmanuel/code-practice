class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        right_bin = list(bin(right))[2:]
        result = [None] * len(right_bin)
        for i in range(len(right_bin) - 1, -1, -1):
            if right_bin[i] == '0':
                result[i] = '0'
            else:
                # right_bin[i] = '0'
                # adj_change = False
                # if i + 1 < len(right_bin) and right_bin[i+1] == '0':
                #     right_bin[i+1] = '1'
                #     adj_change = True
                # temp_num = '0b' + ''.join(right_bin)
                # right_bin[i] = '1'
                # if adj_change:
                #     right_bin[i+1] = '0'
                temp_num = '0b' + ''.join(right_bin[:i]) + '0' + '1' * (len(right_bin) - 1 - i)
                if int(temp_num, 2) >= left:
                    result[i] = '0'
                else:
                    result[i] = '1'
        # print(result)
        result = '0b' + ''.join(result)
        return int(result, 2)