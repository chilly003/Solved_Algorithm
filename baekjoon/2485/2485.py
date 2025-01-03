import sys
from math import gcd
sys.stdin = open('text.txt')


# 입력 처리
N = int(input())
arr = [int(input()) for _ in range(N)]

# 각 가로수 간의 간격 계산
distance = [arr[i+1] - arr[i] for i in range(N-1)]

# 모든 간격의 GCD 계산
gcd_value = distance[0]

for d in distance[1:]:
    gcd_value = gcd(gcd_value, d)

# 추가로 심어야 할 나무 개수 계산
answer = sum((d // gcd_value - 1) for d in distance)

print(answer)