import sys
sys.stdin = open('1388.txt')

#판자 찾는 함수
def find_board(arr, idx, board):
    total = 0
    for i in arr:
        temp = False #판자가 이어지는지 확인하는 참거짓짓
        for j in range(idx):
            
            #판자가 이어진다면 True
            if i[j] == board:
                temp = True
            
            #판자가 끊어진다면 total 더해주고 temp False
            elif temp and i[j] != board:
                total += 1
                temp = False
        #마지막 검사로 temp에 판자가 있는지 확인     
        if temp:
            total += 1

    return total

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
reverse_arr = []

#세로 기준으로 뽑은 행렬렬
for i in range(M):
    temp = ''
    for j in range(N):
        temp += arr[j][i]
    reverse_arr.append(temp)
    temp = ''

print(find_board(arr, M, "-") + find_board(reverse_arr, N, "|"))

if __name__ == '__main__':
    pass