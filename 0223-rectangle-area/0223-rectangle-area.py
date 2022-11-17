class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        top_right_x = min(ax2, bx2)
        top_right_y = min(ay2, by2)
        bottom_left_x = max(ax1, bx1)
        bottom_left_y = max(ay1, by1)
        if top_right_x < bottom_left_x or top_right_y < bottom_left_y:
            area_mid = 0
        else:
            area_mid = (top_right_x - bottom_left_x) * (top_right_y - bottom_left_y)
        # print(top_right_x, bottom_left_x, top_right_y, bottom_left_y)
        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)
        # print(area_1, area_2, area_mid)
        return area_1 + area_2 - area_mid