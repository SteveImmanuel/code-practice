class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people = [(num, i) for i, num in enumerate(groupSizes)]
        people.sort()
        res = []
        i = 0
        while i < len(people):
            people_in_group = people[i][0]
            cur_group = []
            while people_in_group > 0:
                cur_group.append(people[i][1])
                i += 1
                people_in_group -= 1
            res.append(cur_group)
        return res
            