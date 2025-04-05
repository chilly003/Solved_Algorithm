def solution(answers):
    # 각 수포자 패턴 (가변 길이 대응)
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        # 패턴 길이에 맞게 순환 처리
        if ans == p1[i % len(p1)]:
            scores[0] += 1
        if ans == p2[i % len(p2)]:
            scores[1] += 1
        if ans == p3[i % len(p3)]:
            scores[2] += 1
    
    # 최대 점수 및 동점자 추출
    max_score = max(scores)
    return [i+1 for i, score in enumerate(scores) if score == max_score]

if __name__ == '__main__':
    answers = [1,2,3,4,5]
    print(solution(answers))
    answers = [1,3,2,4,2]
    print(solution(answers))