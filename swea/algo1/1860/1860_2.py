import sys
sys.stdin = open('test.txt')

def solution(t):
    N, M, K = map(int, input().split())
    # M초에 K개의 붕어빵
    P = sorted(map(int, input().split()))

    fish = 0

    # 시간이 흘러간다 생각.
    for i in range(P[-1]+1):
        if i % M == 0 and i != 0: #현재 시간이 붕어빵 시간과 같다면 붕어빵 만들기
            fish += K
        if i in P: #손님이 오는 시간과 같다면 붕어빵 제거
            fish -= 1
        if fish < 0: #붕어빵 떨어지면 가게 문 닫아야함.
            print(f'#{t} Impossible')
            return

    print(f'#{t} Possible')

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        solution(t)