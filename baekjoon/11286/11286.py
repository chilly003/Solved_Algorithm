import heapq
import sys
sys.stdin = open('11286.txt')

arr = []

N = int(input())

for _ in range(N):
    x = int(input())

    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)

    else:
        heapq.heappush(arr, (abs(x), x))

