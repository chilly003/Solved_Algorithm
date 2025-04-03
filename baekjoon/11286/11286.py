from collections import deque
import sys
sys.stdin = open('11286.txt')

arr = deque()

N = int(input())
min_int = float("inf")

for _ in range(N):
    now = int(input())
    
    if now != 0:
        if abs(now) <= min_int:
            if now < min_int:
                min_int = now
        arr.append(now)
    # 0인 경우
    else:
        if arr: 
            print(arr.pop(min_int))
        else:
            print(0)
