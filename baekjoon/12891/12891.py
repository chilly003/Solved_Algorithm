import sys
sys.stdin = open('12891.txt')

S, P = map(int, input().split())
DNA_arr = str(input())
A, C, G, T = map(int, input().split())

start = 0
end = P

total = 0
# print(DNA_arr[start:end])
while end != S + 1:
    arr = DNA_arr[start:end]
    answer = True
    
    for i, j in [("A", A), ("C", C), ("G", G), ("T", T)]:
        if arr.count(i) < j:
            answer = False
            break

    if answer:
        total += 1

    start += 1
    end += 1

print(total)
