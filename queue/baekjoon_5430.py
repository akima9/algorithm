import sys
from collections import deque

T = int(sys.stdin.readline())


for i in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    x = input()[1:-1]
    if len(x) > 0:
        x = deque(x.split(','))
    else:
        x = deque([])
    p = deque(list(p))
    cnt = 0
    for k in p:
        if k == 'R':
            cnt += 1
        elif k == 'D':
            if len(x) > 0 :
                if cnt % 2 == 0:
                    x.popleft()
                else:
                    x.pop()
            else:
                print('error')
                break
    if cnt % 2 != 0:
        x.reverse();
    if len(x) > 0:
        print('[',end='')
        for j in range(len(x)):
            if j == (len(x) - 1):
                print(x[j],end='')
            else:
                print(x[j],end=',')
        print(']')