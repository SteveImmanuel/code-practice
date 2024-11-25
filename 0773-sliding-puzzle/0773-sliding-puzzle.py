class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        init_state = tuple(board[0] + board[1])
        finish_state = (1,2,3,4,5,0)
        visited = set()
        queue = deque([(init_state, 0)])

        while len(queue) > 0:
            state, cost = queue.popleft()
            if state in visited:
                continue

            visited.add(state)
            if state == finish_state:
                return cost

            for dir in ['l', 'r', 'u', 'd']:
                next_state = self.move(state, dir)
                if next_state is not None:
                    queue.append((next_state, cost + 1))
        
        return -1

    def move(self, state, direction):
        for i in range(6):
            if state[i] == 0:
                pos = i
                break
        
        new_state = list(state)
        if direction == 'l':
            if pos != 0 and pos != 3:
                new_state[pos], new_state[pos-1] = new_state[pos-1], new_state[pos]
                return tuple(new_state)
        elif direction == 'r':
            if pos != 2 and pos != 5:
                new_state[pos], new_state[pos+1] = new_state[pos+1], new_state[pos]
                return tuple(new_state)

        elif direction == 'u':
            if pos > 2:
                new_state[pos], new_state[pos-3] = new_state[pos-3], new_state[pos]
                return tuple(new_state)

        elif direction == 'd':
            if pos < 3:
                new_state[pos], new_state[pos+3] = new_state[pos+3], new_state[pos]
                return tuple(new_state)
        
        return None