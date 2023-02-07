class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = r = 0
        max_fruit = 0
        cur_fruit = 0
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            cur_fruit += 1
            if len(basket) > 2:
                while len(basket) > 2:
                    basket[fruits[l]] -= 1
                    if basket[fruits[l]] == 0:
                        del basket[fruits[l]]
                    cur_fruit -= 1
                    l += 1
            max_fruit = max(max_fruit, cur_fruit)
        
        return max_fruit
                