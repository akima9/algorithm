
import math
print(math.ceil(1 / 3))
T = int(input()) #테스트케이스

for i in range(T):
    H, W, N = map(int,input().split())
    if N % H == 0:
        Y = H
    else:
        Y = N % H
    X = math.ceil(N / H)

    if X % 10 == X:
        print(Y,end='0')
        print(X)
    else:
        print(Y,end='')
        print(X)