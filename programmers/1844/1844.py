def solution(gems):
    types = set(gems)
    total = len(types)
    
    start, end = 0, 0
    count = {}
    min_length = float('inf')
    answer = [0, 0]
    
    #  end가 gems의 길이보다 크면 종료
    while end < len(gems):
        # end 포인터가 가리키는 보석 추가
        if gems[end] in count:
            count[gems[end]] += 1
        else:
            count[gems[end]] = 1
        end += 1
        
        # 현재 구간에 모든 보석 종류가 포함되었는지 확인
        while len(count) == total:
            # 최소 구간 길이 갱신
            if end - start < min_length:
                min_length = end - start
                answer = [start + 1, end]  # 진열대 번호는 1부터 시작
            
            # start 포인터가 가리키는 보석 제거 및 이동
            count[gems[start]] -= 1
            if count[gems[start]] == 0:
                del count[gems[start]]  # 개수가 0이면 키 삭제
            start += 1
    
    return answer



if __name__ == '__main__':
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))
    gems = ["AA", "AB", "AC", "AA", "AC"]
    print(solution(gems))
    gems = ["XYZ", "XYZ", "XYZ"]
    print(solution(gems))
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))