class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        anchor = coordinates[0]
        anchor_grad = None
        for i in range(1, len(coordinates)):
            if (coordinates[i][0] - anchor[0]) != 0:
                grad = (coordinates[i][1] - anchor[1]) / (coordinates[i][0] - anchor[0])
            else:
                grad = 'inf'
            if anchor_grad is None:
                anchor_grad = grad
            else:
                if type(grad) == type(anchor_grad):
                    if type(anchor_grad) != str:
                        if abs(anchor_grad - grad) > 1e-5:
                            return False
                else:
                    return False
        return True