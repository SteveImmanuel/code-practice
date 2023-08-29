class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_cummulative = [0] * len(customers)
        n_cummulative = [0] * len(customers)
        
        cum_sum = 0
        for i in range(len(customers)):
            if customers[i] == 'N':
                cum_sum += 1
            n_cummulative[i] = cum_sum
        n_cummulative.append(cum_sum)
        
        cum_sum = 0
        for i in range(len(customers) - 1, -1 , -1):
            if customers[i] == 'Y':
                cum_sum += 1
            y_cummulative[i] = cum_sum
        y_cummulative.append(0)            
        
        # print(y_cummulative, n_cummulative)
        penalties = [0] * (len(customers) + 1)
        for i in range(len(penalties)):
            penalties[i] = y_cummulative[i]
            if i > 0:
                penalties[i] += n_cummulative[i - 1]
        # print(penalties)
        return penalties.index(min(penalties))