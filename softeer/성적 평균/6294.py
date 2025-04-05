#성적 평균
import sys
sys.stdin = open('6294.txt')

N, K = map(int, input().split())
S = list(map(int, input().split()))
students = [list(map(int, input().split())) for _ in range(K)]


for i in students:
    all = 0
    #시작 인덱스
    index1 = i[0]-1
    #종료 인덱스
    index2 = i[1]
    for j in range(index1, index2):
        #전체값 만들기
        all += S[j]
    #해당 평균 format을 활용해 출력력
    print(format(all/(i[1]-i[0]+1),".2f"))
