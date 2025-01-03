import sys
sys.stdin = open('2828.txt')

N, M = map(int, input().split())
J = int(input())

total = 0
arr = []
now = 1

for _ in range(J):
    arr.append(int(input()))

for apple in arr:
    if now <= apple and now + (M-1) >= apple:
        pass
    elif now > apple:
        total += abs(apple-now)
        now = apple
    else:
        total += apple - (M-1) - now
        now = apple - (M-1)

print(total)

if __name__ == '__main__':
    pass