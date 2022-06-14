# https://leetcode.com/problems/interleaving-string/

class Solution:
    # TIME LIMIT EXCEEDED
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if s3 == '':
        #     return s1 == '' and s2 == ''

        # pos1 = False
        # pos2 = False

        # if len(s1) > 0 and s1[0] == s3[0]:
        #     pos1 = self.isInterleave(s1[1:], s2, s3[1:])

        # if not pos1 and len(s2) > 0 and s2[0] == s3[0]:
        #     pos2 = self.isInterleave(s1, s2[1:], s3[1:])

        # return pos1 or pos2


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        mem = []
        for _ in range(len(s1) + 1):
            mem.append([False] * (len(s2) + 1))

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i==0 and j==0:
                    mem[i][j] = True
                elif i==0:
                    if s2[j-1] == s3[j-1]:
                        mem[i][j] = mem[i][j-1]
                elif j==0:
                    if s1[i-1] == s3[i-1]:
                        mem[i][j] = mem[i-1][j]
                else:
                    if s1[i-1] == s3[i+j-1]:
                        mem[i][j] = mem[i-1][j]
                    if s2[j-1] == s3[i+j-1]:
                        mem[i][j] = mem[i][j] or mem[i][j-1]

        return mem[len(s1)][len(s2)]




sol = Solution()
s1 = "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
s2 = "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
s3= "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"
# s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
# s1 = 'aabe'
# s2 = 'abee'
# s3 = 'aababeee'
print(sol.isInterleave(s1, s2, s3))