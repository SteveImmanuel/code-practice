class Solution:
    def numberToWords(self, num: int) -> str:
        word_dict = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            0: 'Zero',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }
        
        res = []
        cur_multiplier = 1
        while num > 0:
            num, mod = divmod(num, 1000)
            res.append(self.parse_three(mod, word_dict))
        # print(res)
        final_res = []
        for i in range(len(res) - 1, -1, -1):
            if res[i] == '':
                continue
            final_res.append(res[i])
            multiplier = 1000 ** i
            if multiplier > 1:
                final_res.append(word_dict[multiplier])
        final_res = ' '.join(final_res)
        if final_res == '':
            return 'Zero'
        return final_res
    
#     def numberToWords(self, num: int) -> str:
#         word_dict = {
#             1: 'One',
#             2: 'Two',
#             3: 'Three',
#             4: 'Four',
#             5: 'Five',
#             6: 'Six',
#             7: 'Seven',
#             8: 'Eight',
#             9: 'Nine',
#             0: 'Zero',
#             10: 'Ten',
#             11: 'Eleven',
#             12: 'Twelve',
#             13: 'Thirteen',
#             14: 'Fourteen',
#             15: 'Fifteen',
#             16: 'Sixteen',
#             17: 'Seventeen',
#             18: 'Eighteen',
#             19: 'Nineteen',
#             20: 'Twenty',
#             30: 'Thirty',
#             40: 'Forty',
#             50: 'Fifty',
#             60: 'Sixty',
#             70: 'Seventy',
#             80: 'Eighty',
#             90: 'Ninety',
#             100: 'Hundred',
#             1000: 'Thousand',
#             1000000: 'Million',
#             1000000000: 'Billion'
#         }
        
#         res = deque([])
#         cur_multiplier = 1
#         while num > 0:
#             if num % 100 < 20:
#                 divider = 100
#             else:
#                 divider = 10
                
#             num, mod = divmod(num, divider)
#             if not (mod == 0 and cur_multiplier > 1):
#                 print(mod * cur_multiplier, self.parse(mod, cur_multiplier, word_dict))
#                 res.appendleft(self.parse(mod, cur_multiplier, word_dict))
#             cur_multiplier *= divider
#         res = ' '.join(list(res))
#         print(res)
#         return res
    
    def parse_three(self, num, word_dict):
        # if num in word_dict:
        #     return word_dict[num]
        # else:
        result = []
        hundreds, num = divmod(num, 100)
        # print(hundreds)
        if hundreds > 0:
            result.append(word_dict[hundreds])
            result.append(word_dict[100])

        if num > 0 and num in word_dict:
            result.append(word_dict[num])
        else:
            tens, num = divmod(num, 10)
            if tens > 0:
                result.append(word_dict[tens * 10])
            if num > 0:
                result.append(word_dict[num])
        return ' '.join(result)
            
    
#     def parse(self, num, multiplier, word_dict):
#         real_num = num * multiplier
#         if real_num in word_dict and real_num < 100:
#             return word_dict[real_num]
#         elif multiplier in word_dict:
#             return ' '.join([word_dict[num], word_dict[multiplier]])
#         else:
#             if multiplier > 1000000000:
#                 remaining_multiplier = multiplier // 1000000000
#                 result = word_dict[1000000000]
#             elif multiplier > 1000000:
#                 remaining_multiplier = multiplier // 1000000
#                 result = word_dict[1000000]
#             elif multiplier > 1000:
#                 remaining_multiplier = multiplier // 1000
#                 result = word_dict[1000]
                
#             result = self.parse(num, remaining_multiplier, word_dict) + ' ' + result
#             return result
    
        
        
        