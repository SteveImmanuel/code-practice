class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        cur = 0
        prefix = [None] * len(cost)
        for i in range(len(cost)):
            cur += cost[i]
            prefix[i] = cur
        
        l = 0
        r = 0
        maxlen = 0
        # print(prefix)
        while l < len(prefix):
            r = max(r, l)
            prefix_l = 0
            if l > 0:
                prefix_l = prefix[l-1]
            # print('before',l, r,prefix_l)

            while r < len(prefix) and prefix[r] - prefix_l <= maxCost:
                r += 1
            r = min(r, len(prefix) - 1)
            # print(r)
            if prefix[r] - prefix_l > maxCost:
                r -= 1
            if prefix[r] - prefix_l <= maxCost:
                cur_cost = prefix[r] - prefix_l
                maxlen = max(maxlen, r - l + 1)
                # print('after',l, r, cur_cost, maxlen)
            l += 1
        return maxlen
