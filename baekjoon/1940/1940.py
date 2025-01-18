N = int(input())
M = int(input())
N_arr = sorted(list(map(int, input().split())))

start = 0
end = N - 1
count = 0

# start가 end보다 크면 종료.
while start < end: 
    # 합이 M보다 크면 end를 줄이기
    if N_arr[start] + N_arr[end] > M:
        end -= 1
    # 합이 M보다 작으면 start 키우기
    elif N_arr[start] + N_arr[end] < M:
        start += 1
    # 합이 M과 같다면 카운트 올리고 다른 인덱스 줄이고 키우기
    else:
        count += 1
        start += 1
        end -= 1

print(count)