def get_overall_delivery_time(rows, columns, grid):
  distance_cost_mat = []
  visitation_mat = []
  
  for _ in range(rows):
    distance_cost_mat.append([None] * columns)
    visitation_mat.append([False] * columns)
  
  current_distance = 0
  queue = [current_distance]

  for i in range(rows):
    for j in range(columns):
      if grid[i][j] == 1:
        queue.append((i, j))
        visitation_mat[i][j] = True

  while len(queue) > 0:
    item = queue.pop(0)
    
    if type(item) == int:
      current_distance = item
      if len(queue) > 0:
        queue.append(current_distance + 1)
    else:
      distance_cost_mat[item[0]][item[1]] = current_distance
      if item[0] > 0 and not visitation_mat[item[0] - 1][item[1]]:
        visitation_mat[item[0] - 1][item[1]] = True
        queue.append((item[0] - 1, item[1]))
      if item[0] + 1 < rows and not visitation_mat[item[0] + 1][item[1]]:
        visitation_mat[item[0] + 1][item[1]] = True
        queue.append((item[0] + 1, item[1]))
      if item[1] > 0 and not visitation_mat[item[0]][item[1] - 1]:
        visitation_mat[item[0]][item[1] - 1] = True
        queue.append((item[0], item[1] - 1))
      if item[1] + 1 < columns and not visitation_mat[item[0]][item[1] + 1]:
        visitation_mat[item[0]][item[1] + 1] = True
        queue.append((item[0], item[1] + 1))

  return current_distance - 1, distance_cost_mat

def get_min_overall_delivery_time(rows, columns, grid):
  max_val, distance_cost_mat = get_overall_delivery_time(rows, columns, grid)

  upperbound = max_val
  lowerbound = 0
  k = (upperbound + lowerbound - 1) // 2

  while upperbound != lowerbound:
    x1_plus_y1_min = None
    x1_plus_y1_max = None
    x1_minus_y1_min = None
    x1_minus_y1_max = None


    for i in range(rows):
      for j in range(columns):
        if distance_cost_mat[i][j] > k:
          if x1_plus_y1_max is None or i+j > x1_plus_y1_max[0] + x1_plus_y1_max[1]:
            x1_plus_y1_max = (i,j)
          if x1_plus_y1_min is None or i+j < x1_plus_y1_min[0] + x1_plus_y1_min[1]:
            x1_plus_y1_min = (i,j)
          if x1_minus_y1_max is None or i-j > x1_minus_y1_max[0] - x1_minus_y1_max[1]:
            x1_minus_y1_max = (i,j)
          if x1_minus_y1_min is None or i-j < x1_minus_y1_min[0] - x1_minus_y1_min[1]:
            x1_minus_y1_min = (i,j)
 
    possible = False
    i = 0
    j = 0
    candidates = [x1_plus_y1_max, x1_plus_y1_min, x1_minus_y1_max, x1_minus_y1_min]
    while not possible and i < rows:
      j = 0
      while not possible and j < columns:
        # print('ij2',i,j)
        if grid[i][j] == 0:
          distances = map(lambda x: manhattan_distance(x, (i,j)), candidates)
          max_dist = max(distances)
          # print(max_dist)
          if max_dist <= k:
            possible = True
            # print(candidates)
            # print(list(distances))
            # print(k, i, j, max_dist)
            break
        j += 1
      i += 1
      
    if possible:
      upperbound = k
    else:
      lowerbound = k + 1

    k = (upperbound + lowerbound - 1) // 2
  
  return lowerbound

def manhattan_distance(point1, point2):
  return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def brute_force(rows, columns, grid):
  overall_distance, _ = get_overall_delivery_time(rows, columns, grid)
  old_grid = grid.copy()
  idxs = (0,0)
  for i in range(rows):
      for j in range(columns):
          if grid[i][j] != 1:
              grid[i][j] = 1
              cur_dist, _ = get_overall_delivery_time(rows, columns, grid)
              if cur_dist < overall_distance:
                overall_distance = cur_dist
                idxs = (i,j)
              grid[i][j] = 0
  # print('gt:',idxs)
  return overall_distance  

def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the grid dimensions
    rows, columns = map(int, input().split())
    # Get the grid
    grid = [list(map(int, input())) for _ in range(rows)]
    print(f'Case #{t+1}:', get_min_overall_delivery_time(rows, columns, grid))

if __name__ == '__main__':
  main()