class Solution {
public:
    int numberOfChild(int n, int k) {
        int curChild = 0;
        int direction = 1;
        for(int i = 0; i < k; i++) {
            if (curChild + direction == n) {
                direction = -1;
            } else if (curChild + direction == -1) {
                direction = 1;
            } 
            curChild += direction;
        }
        return curChild;
    }
};