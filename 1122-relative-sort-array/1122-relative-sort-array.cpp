class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> result;
        int occ[1005];
        for (auto num: arr1) {
            occ[num]++;
        }
        for (auto num: arr2) {
            result.insert(result.end(), occ[num], num);
            occ[num] = 0;
        }
        for (int i=0;i<1005;i++) {
            result.insert(result.end(), occ[i], i);
        }
        return result;
    }
};