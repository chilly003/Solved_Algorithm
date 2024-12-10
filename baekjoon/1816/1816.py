import sys

sys.stdin = open('test.txt')


def find(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    primes = []

    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False
    return primes


def prime(n, checks):
    factors = []
    for check in checks:
        if check * check > n:  # 더 이상 나눌 필요가 없음
            break
        while n % check == 0:
            factors.append(check)
            n //= check
    if n > 1:  # 마지막으로 남은 소수가 있다면 추가
        factors.append(n)
    return factors


T = int(input())
for _ in range(1, T + 1):
    num = int(input())

    list2 = find(10 ** 6)
    last = prime(num, list2)

    # 모든 소인수가 10^6보다 큰지 확인
    if all(answer > 10 ** 6 for answer in last):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    pass