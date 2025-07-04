import sys
sys.stdin = open("1260.txt")
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
check = [0] * (N+1)
dfs_answer = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

def DFS(num):
    dfs_answer.append(num)
    check[num] = 1
    for i in graph[num]:
        if check[i] == 0:
            DFS(i)

DFS(V)
print(*dfs_answer)

check = [0] * (N+1)
bfs_answer = []

def BFS(num):
    queue = deque()
    queue.append(num)
    check[num] = 1
    # 인접한 그래프 우선으로 탐색
    while queue:
        node = queue.popleft()
        bfs_answer.append(node)
        for i in graph[node]:
            if check[i] == 0:
                check[i] = 1
                queue.append(i)

BFS(V)
print(*bfs_answer)