class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        gb_dict = []
        gb_range = {}
        gb_types = ['G', 'M', 'P']
        
        for i, g in enumerate(garbage):
            gb_dict.append(Counter(g))
            for gb_type in gb_types:
                if gb_type in gb_dict[i]:
                    gb_range[gb_type] = i
        
        total_time = 0
        for gb_type in gb_types:
            if gb_type not in gb_range:
                continue
                
            house_idx = 0
            cur_time = 0
            while house_idx <= gb_range[gb_type]:
                cur_time += gb_dict[house_idx][gb_type]
                if house_idx < gb_range[gb_type]:
                    cur_time += travel[house_idx]
                house_idx += 1
            total_time += cur_time
        return total_time