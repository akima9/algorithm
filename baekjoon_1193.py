X = int(input())
cnt = 0
sumCnt = 0

while sumCnt < X:
    cnt += 1
    sumCnt += cnt
    prevSumCnt = sumCnt - cnt

if cnt % 2 == 0:
    print(X - prevSumCnt,end='/')
    print(cnt - (X - prevSumCnt - 1))
else:
    print(cnt - (X - prevSumCnt - 1),end='/')
    print(X - prevSumCnt)
