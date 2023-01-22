class Solution:
    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

    def partition(self, s: str) -> List[List[str]]:
        mem = defaultdict(lambda: set())
        res = self.partitionRec(s, mem)
        return res

    def partitionRec(self, s, mem):
        if s not in mem:

            if self.is_palindrome(s):
                mem[s].add((s,))

            for i in range(1, len(s)):
                head = s[:i]
                tail = s[i:]

                head_res = self.partitionRec(head, mem)
                tail_res = self.partitionRec(tail, mem)

                for res1 in head_res:
                    for res2 in tail_res:
                        candidate = tuple(res1 + res2)
                        mem[s].add(candidate)

        return mem[s]