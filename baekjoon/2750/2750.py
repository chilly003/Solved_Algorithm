import sys
sys.stdin = open('2750.txt')

N = int(input())

arr = [int(input()) for _ in range(N)]

a = N
while a != 1:
    for i in range(a - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    a -= 1

for i in range(N):
    print(arr[i])