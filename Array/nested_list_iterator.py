class NestedIterator:
    def __init__(self, nestedList):
        self.it = 0
        self.arr = self.unpack(nestedList)        
    
    def next(self) -> int:
        self.it += 1
        return self.arr[self.it-1]
    
    def hasNext(self) -> bool:
        return self.it < len(self.arr)

    def unpack(self, nestedList):
        res = []
        for el in nestedList:
            if type(el) == list:
                res += self.unpack(el)
            else:
                res.append(el)
        return res
                
         

nestedList = [[1,1],2,[1,[1], [1,[2],[3,4]]]]
ni = NestedIterator(nestedList)
res = []
while ni.hasNext():
    res.append(ni.next())
print(res)