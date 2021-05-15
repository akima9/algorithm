testCase = int(input())

for t in range(testCase):
    x, y = map(int,input().split())
    k = 1
    cnt = 0
    temp = x
    while True:
        if temp + k >= y:
            if temp + k >= y:
                k = 1
                temp += k
                k += 1
            else:
                k -= 1
                temp += k
                k += 1
        else:
            temp += k
            k += 1
        cnt += 1
        
        if temp == y:
            break
    print(cnt)