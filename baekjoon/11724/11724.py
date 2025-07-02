import sys
sys.stdin = open("11724.txt")

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
graph = [0]*(N+1)

def DFS(num):
    graph[num] = 1
    for i in A[num]:
        if graph[i] == 0:
            DFS(i)

for _ in range(M):
    u,v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

answer = 0

for i in range(1, N+1):
    if graph[i] == 0:
        answer += 1
        DFS(i)

print(answer)