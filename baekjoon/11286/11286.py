from collections import deque
import sys
sys.stdin = open('11286.txt')

arr = deque()

N = int(input())

for _ in range(N):
    arr.append(int(input()))
    min_now = 