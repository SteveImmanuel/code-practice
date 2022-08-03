# https://leetcode.com/problems/my-calendar-i/
import bisect

class MyCalendar:
    def __init__(self):
        self.start_arr = []
        self.end_arr = []
        
    def book(self, start: int, end: int) -> bool:
        if len(self.start_arr) == 0:
            self.start_arr.append(start)
            self.end_arr.append(end)
            return True
        else:
            idx = bisect.bisect_right(self.end_arr, start)
            # print(idx)
            if idx != len(self.end_arr):
                # print(self.start_arr)
                # print(end, self.start_arr[idx])
                if end <= self.start_arr[idx]:
                    self.start_arr.insert(idx, start)
                    self.end_arr.insert(idx, end)
                    return True
                else:
                    return False
            else:
                self.start_arr.append(start)
                self.end_arr.append(end)
                return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(1,2)
print(param_1)
print(obj.start_arr)
print(obj.end_arr)
param_1 = obj.book(2,3)
print(param_1)
print(obj.start_arr)
print(obj.end_arr)
param_1 = obj.book(3,4)
print(param_1)
print(obj.start_arr)
print(obj.end_arr)
param_1 = obj.book(3,5)
print(param_1)
print(obj.start_arr)
print(obj.end_arr)