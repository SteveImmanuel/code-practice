tc = int(input())

for i in range(1, tc + 1):
    N, M = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))
    total_candy = sum(C)
    print(f'Case #{i}: {total_candy % M}')