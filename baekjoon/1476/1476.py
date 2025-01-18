E, S, M = map(int, input().split())
year = 1

while True:
    #지정한 year에 인풋을 -하고 최댓값을 나눴을 때 0이 되어야 지구 년도가 나옴.
    if (year-E) % 15 == 0 and (year-S) % 28 == 0 and (year-M) % 19 == 0:
        break
    year += 1

print(year)

if __name__ == '__main__':
    pass