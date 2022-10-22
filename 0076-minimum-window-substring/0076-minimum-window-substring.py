class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        counter_t = Counter(t)
        counter_s = defaultdict(int)
        while len(counter_t) > 0 and r < len(s):
            counter_s[s[r]] += 1
            if s[r] in counter_t:
                counter_t[s[r]] -= 1
                if counter_t[s[r]] == 0:
                    del counter_t[s[r]]
            r += 1
        
        if len(counter_t) > 0:
            return ''

        counter_t = Counter(t)
        for key, val in counter_t.items():
            counter_s[key] -= val

        while counter_s[s[l]] > 0:
            counter_s[s[l]] -= 1
            l += 1

        current_min = (l, r-1)
        for i in range(r, len(s)):
            counter_s[s[i]] += 1

            while counter_s[s[l]] > 0:
                counter_s[s[l]] -= 1
                l += 1

            if i - l + 1 < current_min[1] - current_min[0] + 1:
                current_min = (l, i)
        
        return s[current_min[0]:current_min[1]+1]