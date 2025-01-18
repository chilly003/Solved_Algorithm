def find_N(index, point1, point2):
    #index를 제외한 요소의 합을 확인.
    while point1 < point2:
        if point1 == index:
            point1 += 1
        
        elif point2 == index:
            point2 -= 1

        elif N_arr[index] == N_arr[point1] + N_arr[point2]:
            return 1
        
        elif N_arr[index] < N_arr[point1] + N_arr[point2]:
            point2 -= 1
            
        else:
            point1 += 1

    return 0

N = int(input())
N_arr = list(map(int, input().split()))
#투포인터는 정렬이 우선. 잊지말자^^
N_arr.sort()

N_len = len(N_arr)
count = 0

for i in range(N_len):
    check = find_N(i, 0, N_len - 1)
    count += check

print(count)