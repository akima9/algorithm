import sys
from collections import deque
R = deque([])
N = int(sys.stdin.readline())

for i in range(N):
    M = sys.stdin.readline().split()
    if M[0] == 'push_front':
        R.appendleft(M[1])
    elif M[0] == 'push_back':
        R.append(M[1])
    elif M[0] == 'pop_front':
        if len(R) > 0:
            print(R.popleft())
        else:
            print(-1)
    elif M[0] == 'pop_back':
        if len(R) > 0:
            print(R.pop())
        else:
            print(-1)
    elif M[0] == 'size':
        print(len(R))
    elif M[0] == 'empty':
        if len(R) > 0:
            print(0)
        else:
            print(1)
    elif M[0] == 'front':
        if len(R) > 0:
            print(R[0])
        else:
            print(-1)
    elif M[0] == 'back':
        if len(R) > 0:
            print(R[-1])
        else:
            print(-1)
