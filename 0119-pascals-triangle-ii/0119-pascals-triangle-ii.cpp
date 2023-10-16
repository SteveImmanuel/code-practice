class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) {
            return {1};
        } else {
            vector<int> prevRow = getRow(rowIndex - 1);
            vector<int> middle;
            for(int i = 0; i < prevRow.size() - 1; i++){
                middle.push_back(prevRow[i] + prevRow[i+1]);
            }
            middle.insert(middle.begin(), 1);
            middle.push_back(1);
            return middle;
        }
    }
};


// class Solution:
//     def getRow(self, rowIndex: int) -> List[int]:
//         if rowIndex == 0:
//             return [1]
//         else:
//             prev_row = self.getRow(rowIndex - 1)
//             middle = []
//             for i in range(len(prev_row) - 1):
//                 middle.append(prev_row[i] + prev_row[i+1])
//             return [1] + middle + [1]