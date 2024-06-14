class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int total = 0;
        int lastNum = nums[0];
        for(int i = 1; i<nums.size(); i++) {
            if (nums[i] <= lastNum) {
                total += lastNum + 1 - nums[i];
                lastNum++;
            } else {
                lastNum = nums[i];
            }
        }
        return total;
    }
};