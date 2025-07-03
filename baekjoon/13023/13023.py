import sys

from mpmath.calculus.differentiation import dpoly

sys.stdin = open("13023.txt")

N, M = map(int, input().split())
friend = [[] for _ in range(N)]
check = [0] * (N)
answer = 0

def DFS(num, depth):
    global answer

    if depth == 5:
        answer = 1
        return

    check[num] = 1
    for i in friend[num]:
        if check[i] == 0:
            DFS(i, depth+1)
    check[num] = 0

for i in range(M):
    a, b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(N):
    DFS(i, 1)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)