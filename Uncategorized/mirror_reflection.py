# https://leetcode.com/problems/mirror-reflection/
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        current_height = q
        on_left_wall = False
        going_up = False

        mod_height = -1
        while mod_height != 0:
            going_up = not going_up
            current_height = q - mod_height if mod_height != -1 else q

            remaining_height = p - current_height
            mod_height = remaining_height % q
            total_reflection = int(remaining_height // q)

            if total_reflection % 2 != 0:
                on_left_wall = not on_left_wall

        if going_up:
            if on_left_wall:
                return 2
            else:
                return 1
        else:
            return 0

sol = Solution()
print(sol.mirrorReflection(5,2))