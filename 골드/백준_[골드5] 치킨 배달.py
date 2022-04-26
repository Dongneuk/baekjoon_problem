from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))


min_d = float("inf")

for ch in combinations(chicken, M):

    sum_d = 0
    for home in house:
        sum_d += min([abs(i[0] - home[0]) + abs(i[1] - home[1]) for i in ch])
        if min_d <= sum_d:
            break
    if sum_d < min_d:
        min_d = sum_d

print(min_d)

## 시간복잡도: O(NM) 