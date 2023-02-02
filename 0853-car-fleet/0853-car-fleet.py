class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, spd, 0] for pos, spd in zip(position, speed)]
        cars.sort(key=lambda x:x[0])
        # print(cars)
        total_fleet = 0
        while len(cars) > 0:
            front = cars.pop()
            if len(cars) > 0:
                back = cars.pop()
                if back[2] < front[2]:
                    back[0] += back[1] * (front[2] - back[2])
                    back[2] = front[2]
                    
                if back[0] >= front[0]:
                    cars.append(front)
                else:
                    if front[1] >= back[1]:
                        total_fleet += 1
                        cars.append(back)
                    else:
                        meet_distance = (front[1] * (front[0] - back[0])) / (back[1] - front[1])
                        if front[0] + meet_distance > target:
                            total_fleet += 1
                            cars.append(back)
                        else:
                            delta_time = meet_distance / front[1]
                            front[0] += meet_distance
                            front[2] += delta_time
                            cars.append(front)
            else:
                total_fleet += 1
            # print(cars)
            
        return total_fleet