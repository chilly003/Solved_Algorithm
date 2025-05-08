import sys
sys.stdin = open("5639.txt")

# 입력 받기
numbers = list(map(int, sys.stdin.read().split()))

# 후위 순회 결과를 저장할 리스트
result = []


# 후위 순회 함수 (재귀)
def postorder(start, end):
    if start > end:
        return

    # 루트 노드
    root = numbers[start]

    # 오른쪽 서브트리 시작 인덱스 찾기
    idx = start + 1
    while idx <= end and numbers[idx] < root:
        idx += 1

    # 왼쪽 서브트리 후위 순회
    postorder(start + 1, idx - 1)

    # 오른쪽 서브트리 후위 순회
    postorder(idx, end)

    # 루트 노드 추가 (후위 순회는 루트가 마지막)
    result.append(root)


# 전체 트리에 대해 후위 순회 실행
postorder(0, len(numbers) - 1)

# 결과 출력
for num in result:
    print(num)
