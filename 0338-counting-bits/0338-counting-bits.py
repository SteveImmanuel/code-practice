class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [None for _ in range(n+1)]
        cur_biggest_power_two = 2
        for i in range(n+1):
            if i == 0:
                result[i] = 0
            elif i == 1:
                result[i] = 1
            elif i == 2:
                result[i] = 1
            else:
                closest_power_two = cur_biggest_power_two & i
                # print(i, cur_biggest_power_two, i - closest_power_two)
                if closest_power_two > 0:
                    result[i] = result[cur_biggest_power_two] + result[i - closest_power_two]
                else:
                    result[i] = 1
                    cur_biggest_power_two = i
                    
        return result