N = 4
odd = [1,3,5,7,9]

def DFS(num):
    str_num = str(num)
    int_num = int(num)

    #소수인지 num의 절반값을 나눠가면서 확인
    for check in range(2, int((int_num/2)+1)):
        if int_num % check == 0:
            return
    #만약 N의 자릿수와 같으면 프린트
    if len(str_num) == N:
        return print(int_num)
    #아니라면 재귀함수로 넘어가기
    else:
        for i in odd:
            new_num = str(num) + str(i)
            DFS(new_num)

DFS(2)
DFS(3)
DFS(5)
DFS(7)
