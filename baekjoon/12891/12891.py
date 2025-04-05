import sys
sys.stdin = open('12891.txt')

S, P = map(int, input().split())
DNA_arr = str(input())
A, C, G, T = map(int, input().split())
total = 0
ACGT_st = {"A":A, "C":C,"G":G,"T":T}
ACGT = {"A":0, "C":0,"G":0,"T":0}

start = 0
end = P - 1

answer = True
for i, j in [("A", A), ("C", C), ("G", G), ("T", T)]:
    a = DNA_arr[start:end+1].count(i) #end 부분 +1 해야함. 밑에는 슬라이싱 안해서 다소 번거롭
    ACGT[i] = a
    if a < j:
        answer = False

if answer:
    total += 1


for _ in range(S-P):
    start += 1
    end += 1

    a = DNA_arr[start - 1] #이동하기 전 요소를 빼야함.
    b = DNA_arr[end]

    ACGT[a] -= 1
    ACGT[b] += 1

    answer = True
    for key in ACGT:  # 모든 문자 검사
        if ACGT[key] < ACGT_st[key]:
            answer = False
            break
    
    if answer:
        total += 1

print(total)
