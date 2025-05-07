import sys
sys.stdin = open("5639.txt")

numbers = list(map(int, sys.stdin.read().split()))

mid = len(numbers//2)
root = mid - 2
left = mid - 1
right = 0

# 일단 첫 숫자만 넣을 거임
answer = [numbers[left]]

# root가 0일 때까지 반복
# 근데 이렇게 하면 오른쪽 왼쪽이 없는 그래프는 어케찾음?
# 오른쪽, 왼쪽을 임의 지정해서 root보다 작거나 큰걸로 위치 구분 후 넣기??
# 근데 이게 처음 root를 지정하고 넣으면 그 root는 다음 root의 left임. 이거구분할 필요가 없지않나?
while root != 0:
    if numbers[root + 1]:
        right = root + 1


print(answer)