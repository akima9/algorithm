n = int(input())
for i in range(n):
    a = list(input())
    cnt = 0
    sum = 0
    for j in a:
        if j == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)