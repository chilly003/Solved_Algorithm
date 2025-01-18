N = int(input())
count = 1
start = 1
end = 1
sum = 1

# 다행이 연속된 자연수라 start, end 변수 수가 그냥 그 자연수임.
# end가 자연수 N이면 멈추기(이미 카운트에 자기 자신이 들어감)
while end != N:
    # 합이 N과 같으면 카운트 올리고 elif 조건을 보기 위해 end값을 sum에 올림
    # 1,2,3의 합이 N이면 end을 올려서 1,2,3,4로 변경 그러면 elif로 가 확인
    if sum == N:
        count += 1
        end += 1
        sum += end
    #합이 N보다 크면 sum에서 start 부분을 빼고 start를 크게한다.
    elif sum > N:
        sum -= start
        start += 1
    #합이 N보다 작으면 end를 키운다.
    else:
        end += 1
        sum += end

print(count)
