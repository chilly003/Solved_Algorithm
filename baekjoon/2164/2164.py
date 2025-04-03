from collections import deque

N = int(input())

card_arr = deque(i for i in range(1, N+1))

while len(card_arr) != 1:
    card_arr.popleft()
    card_arr.append(card_arr.popleft())

print(card_arr[0])