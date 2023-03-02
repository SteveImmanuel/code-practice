class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr_cur_char = 0
        total_cur_char = 1
        
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[ptr_cur_char]:
                total_cur_char += 1
            else:
                ptr_digits = ptr_cur_char + 1

                if total_cur_char > 1:
                    digits = []
                    while total_cur_char > 0:
                        digits.append(total_cur_char % 10)
                        total_cur_char = total_cur_char // 10
                    for j in range(len(digits) - 1, -1, -1):
                        chars[ptr_digits] = str(digits[j])
                        ptr_digits += 1
                
                if i < len(chars):
                    ptr_cur_char = ptr_digits
                    chars[ptr_cur_char] = chars[i]
                    total_cur_char = 1    
                
        return ptr_digits
                
                
                
                