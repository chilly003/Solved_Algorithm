import sys
sys.stdin = open('1874.txt')

N = int(input())
arr = [int(input()) for _ in range(N)]
answer = []
pt_arr = []
num = 1

for target in arr:
    #타겟 숫자보다 num이 작다면
    while target >= num:
        pt_arr.append(num)
        answer.append("+")
        num += 1

    #타겟 넘버와 배열의 마지막 요소가 같다면
    if pt_arr[-1] == target:
        pt_arr.pop()
        answer.append('-')

    #전부 불가능할 경우
    else:
        print('NO')
        break

#\n 띄어쓰기기
else:
    print('\n'.join(answer))