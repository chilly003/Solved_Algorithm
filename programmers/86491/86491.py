def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)


if __name__ == '__main__':
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(sizes))
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes))