class Solution:
    def get_roman(self, num, roman_dict):
        if num in roman_dict:
            return roman_dict[num]
        
        res = ''
        for key in roman_dict.keys():
            quotient, remainder = divmod(num, key)
            if quotient == 0:
                continue
            
            res += roman_dict[key] * quotient
            
            if remainder == 0:
                break
            else:
                num = remainder
        return res
            
    
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        
        res = ''
        multiplier = 1
        while num > 0:
            remainder = num % 10
            roman = self.get_roman(remainder * multiplier, roman_dict)
            res = roman + res

            multiplier *= 10
            num //= 10
        
        return res
            
            
        
        
        