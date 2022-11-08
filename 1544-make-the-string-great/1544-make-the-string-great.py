class Solution:
    def makeGood(self, s: str) -> str:
        str_list = list(s)
        
        removed_idx = set()
        bad_exist = True
        
        while bad_exist:
            bad_exist = False
            f_idx = None
            s_idx = None
        
            for i in range(len(s)):
                if i in removed_idx:
                    continue

                if f_idx is None:
                    f_idx = i
                else:
                    s_idx = i
                    
                    # print(f_idx, s_idx)
                    if abs(ord(str_list[f_idx]) - ord(str_list[s_idx])) == 32:
                        removed_idx.add(f_idx)
                        removed_idx.add(s_idx)

                        f_idx = None
                        s_idx = None
                        bad_exist = True
                    else:
                        f_idx = s_idx

                # print(removed_idx)
        res = ''
        for i in range(len(str_list)):
            if i not in removed_idx:
                res += str_list[i]
        return res
                
                