c = int(input())
for i in range(c):
    a = list(map(int,input().split()))
    sumA = sum(a[1:])
    avgA = (sumA // a[0])
    cnt = 0
    for j in a[1:]:
        if j > avgA:
            cnt += 1
    result = (cnt / a[0]) * 100
    print('{:.3f}%'.format(result))