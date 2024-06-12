class Solution {
public:
    int valueAfterKSeconds(int n, int k) {
        int mem[k+1][n];
        long long MOD = 1000000007;
        for (int i=0;i<=k;i++){
            for (int j=0;j<n;j++){
                if (i==0 | j==0) {
                    mem[i][j] = 1;
                } else {
                    mem[i][j] = (mem[i][j-1] + mem[i-1][j]) % MOD;
                }
            }
        }
        return mem[k][n-1];
    }
};