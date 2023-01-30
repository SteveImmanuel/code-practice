class Solution:
    def checkValidString(self, s: str) -> bool:
        total_left = 0
        chance = 0
        ltr = None
        for char in s:
            if char == '(':
                total_left += 1
            elif char == ')':
                if total_left > 0:
                    total_left -= 1
                elif chance > 0:
                    chance -= 1
                else:
                    ltr = False
                    break
            else:
                chance += 1    
        if ltr is None:    
            ltr = total_left <= chance
        
        total_right = 0
        chance = 0
        rtl = None
        for char in s[::-1]:
            if char == '(':
                if total_right > 0:
                    total_right -= 1
                elif chance > 0:
                    chance -= 1
                else:
                    rtl = False
                    break
            elif char == ')':
                total_right += 1
            else:
                chance += 1    
        if rtl is None:    
            rtl = total_right <= chance
        
        return ltr and rtl
        