class StockSpanner:

    def __init__(self):
        self.history = []        

    def next(self, price: int) -> int:
        val = 1
        if len(self.history) > 0:
            i = len(self.history) - 1
            while i >= 0:
                if self.history[i][0] <= price:
                    val += self.history[i][1]
                    i -= self.history[i][1]
                else:
                    break
            
        
        self.history.append((price, val))
        return val
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)