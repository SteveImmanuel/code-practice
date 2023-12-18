class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_mapping = {}
        self.cuisine_heap = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_mapping[food] = [rating, cuisine]
            heapq.heappush(self.cuisine_heap[cuisine], (-rating, food))
        
        # for c in self.cuisine_heap:
        #     print(c, self.cuisine_heap[c])

    def changeRating(self, food: str, newRating: int) -> None:
        # print('changing', food, 'to', newRating)
        old_rating, c = self.food_mapping[food]
        self.food_mapping[food][0] = newRating
        # print('before', self.cuisine_heap[c])
        heapq.heappush(self.cuisine_heap[c], (-newRating, food))
        # print('after', self.cuisine_heap[c])
        
        
    def highestRated(self, cuisine: str) -> str:
        found = False
        while not found:
            rating, food = self.cuisine_heap[cuisine][0]
            rating *= -1
            if self.food_mapping[food][0] == rating:
                found = True
            else:
                heapq.heappop(self.cuisine_heap[cuisine])
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)