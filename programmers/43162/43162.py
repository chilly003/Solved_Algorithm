def dfs(index, n, computers, check):
    global answer
    check[index] = 1
    for i in range(n):
        if computers[index][i] == 1 and not check[i]:
            answer -= 1
            dfs(i, n, computers, check)

def solution(n, computers):
    global answer
    answer = n
    check = [0] * n

    for i in range(n):
        if not check[i]:
            dfs(i, n, computers, check)

    return answer

if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))

    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))

    n = 4
    computers = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    print(solution(n, computers)) 
