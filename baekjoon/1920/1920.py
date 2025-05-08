import sys
sys.stdin = open("1920.txt")

N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_num = list(map(int, input().split()))
A.sort() #정렬 이분탐색 할거임.

start = 0
end = len(A) - 1
mid = (start + end) // 2


def find(num, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if num == A[mid]:
        return 1
    # 시작과 중간 사이의 숫자
    elif num >= A[start] and num < A[mid]:
        return find(num, start, mid - 1)
    # 중간과 끝 사이의 숫자
    else:
        return find(num, mid + 1, end)


for num in M_num:
    answer = find(num, start, end)
    print(answer)