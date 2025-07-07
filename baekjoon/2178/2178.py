import sys
sys.stdin = open("2178.txt")
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
check = [[0 for _ in range(M)] for _ in range(N)]
maps = [[0]* M for _ in range(N)]

for i in range(N):
    num = list(input())
    for j in range(M):
        maps[i][j] = int(num[j])

def BFS(x, y):
    now = deque()
    now.append([x,y])
    check[x][y] = 1
    while now:
        resent = now.popleft()
        now_x = resent[0]
        now_y = resent[1]
        for i in range(4):
            xi = now_x+ dx[i]
            yj = now_y+ dy[i]
            if 0 <= xi < N and 0 <= yj < M:
                if check[xi][yj] == 0 and maps[xi][yj] == 1:
                    check[xi][yj] = 1
                    maps[xi][yj] = maps[now_x][now_y] + 1
                    now.append([xi, yj])

BFS(0, 0)
print(maps[N-1][M-1])