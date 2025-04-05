N = int(input())
arr = list(map(int, input().split()))

answer = [-1] * N
stack = []

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        a = stack.pop()
        answer[a] = arr[i]
    stack.append(i)

print(*answer)
