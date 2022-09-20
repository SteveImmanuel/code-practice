# https://leetcode.com/problems/find-duplicate-file-in-system/

from typing import List
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = defaultdict(lambda: [])
        for path in paths:
            info = path.split(' ')
            dir = info[0]
            for i in range(1, len(info)):
                file = info[i].split('(')
                content = file[-1][:-1]
                filename = file[0]
                content_dict[content].append(f'{dir}/{filename}')
        all_groups = list(filter(lambda group: len(group)>1, content_dict.values()))
        return all_groups

sol = Solution()
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
# paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
print(sol.findDuplicate(paths))