import sys
sys.stdin = open('sample_input.txt')

def dfs(row):
    if row >= N:
        global cnt
        cnt += 1
        return
 
    for col in range(N):
        if cols[col] or diag1[row + col] or diag2[row - col]:
            continue
        cols[col] = diag1[row + col] = diag2[row - col] = 1
        dfs(row+1)
        cols[col] = diag1[row + col] = diag2[row - col] = 0

N = int(input())
cnt = 0
cols = [0 for _ in range(N)]
diag1 = [0 for _ in range(2 * N - 1)]
diag2 = [0 for _ in range(2 * N - 1)]

dfs(0)
print(cnt)