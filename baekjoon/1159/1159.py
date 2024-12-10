import sys

sys.stdin = open('1159.txt')

alphabet = [0] * 26
answer = ''

T = int(input())
for _ in range(0, T):
    first_name = str(input())
    alphabet[ord(first_name[0])-97] += 1

for find in range(26):
    if alphabet[find] >= 5:
        answer += chr(find + 97)

if answer:
    print(answer)
else:
    print('PREDAJA')


if __name__ == '__main__':
    pass