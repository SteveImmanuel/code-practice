class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            prev_row = self.getRow(rowIndex - 1)
            middle = []
            for i in range(len(prev_row) - 1):
                middle.append(prev_row[i] + prev_row[i+1])
            return [1] + middle + [1]