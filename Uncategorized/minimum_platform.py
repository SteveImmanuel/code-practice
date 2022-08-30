# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

from bisect import bisect_right
import heapq

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    # TLE O(n^2 log n)
    # def minimumPlatform(self,n,arr,dep):
    #     platform = []
    #     train_time = [(a, d) for a, d in  zip(arr, dep)]
    #     train_time.sort(key=lambda x: x[0])
        
    #     for train in train_time:
    #         if len(platform) == 0:
    #             platform.append([train])
    #         else:
    #             # platform is always sorted by latest train departure
    #             insert_idx = self.find_platform(platform, train)
    #             if insert_idx != 0:
    #                 platform[insert_idx - 1].append(train)
    #             else:
    #                 platform.append([train])

    #             platform.sort(key=lambda x: x[-1][1])
    #         print(platform)
    #     return len(platform)

    # def find_platform(self, platform, train):
    #     platform_dep = [x[-1][1] for x in platform]
    #     return bisect_right(platform_dep, train[0])

    def minimumPlatform(self,n,arr,dep):
        platform = []
        train_time = [(a, d) for a, d in  zip(arr, dep)]
        train_time.sort(key=lambda x: x[0])
        heapq.heappush(platform, train_time[0][1])
        for i in range(1, len(train_time)):
            min_el = heapq.heappop(platform)
            if train_time[i][0] <= min_el:
                heapq.heappush(platform, min_el)
            
            heapq.heappush(platform, train_time[i][1])
            print(platform)
        return len(platform)


sol = Solution()
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1000, 1120, 1130, 1900, 2000]
# arr = [900, 1100, 1235]
# dep = [1000, 1200, 1240]
# arr = [5,0,25,35]
# dep = [10,20,40,45]
print(sol.minimumPlatform(6, arr, dep))