class Solution {
public:
    void sortColors(vector<int>& nums) {
        int occ[3];
        for (auto num: nums) {
            occ[num]++;
        }
        int idx = 0;
        for (int i=0;i<3;i++) {
            int curCount = 0;
            while (curCount < occ[i]) {
                nums[idx] = i;
                curCount++;
                idx++;
            }
        }
    }
};