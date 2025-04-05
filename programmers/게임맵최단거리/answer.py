mapdel = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs(maps, count, index, end, answer):
    if index == end:
        answer.append(count)
        return answer
    
    for di, dj in mapdel:
        wi = index[0] + di
        wj = index[1] + dj
        #좌표가 범위에 들어가는지, 길이 맞는지 확인인
        if 0 <= wi < len(maps) and 0 <= wj < len(maps[0]) and maps[wi][wj] == 1:
            maps[wi][wj] = 0
            bfs(maps, count + 1, [wi, wj], end, answer)
            maps[wi][wj] = 1

    return answer

def solution(maps):
    answer = []
    end = [len(maps) - 1 ,len(maps[0]) - 1]
    real = bfs(maps, 1, [0,0], end, answer)

    if real:
        return min(real)
    else:
        return -1


if __name__ == '__main__':
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    print(solution(maps))