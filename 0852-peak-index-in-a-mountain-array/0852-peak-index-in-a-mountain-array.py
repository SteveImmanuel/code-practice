class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.peak_idx(arr, 0, len(arr) - 1)
        
    def peak_idx(self, arr, l, r):
        while l < r:
            m = (l + r) // 2
            # print(l, m, r, arr[l], arr[m], arr[r])
            if arr[m] > arr[l] and arr[m] > arr[r]:
                l_res = self.peak_idx(arr, l, m)
                r_res = self.peak_idx(arr, m, r)
                # print('lres',l_res)
                # print('rres',r_res)
                if arr[l_res] > arr[r_res]:
                    return l_res
                else:
                    return r_res
                
            else:
                if arr[l] >= arr[m] and arr[l] > arr[r]:
                    r = m
                else: # if arr[r] > arr[m] and arr[r] > arr[l]:
                    l = m + 1
        return l