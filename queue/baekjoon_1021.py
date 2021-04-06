from collections import deque

N,M = list(map(int,input().split()))
Q = deque([i for i in range(1,N+1)])
A = deque(list(map(int,input().split())))
cnt = 0

while len(A) > 0:
    if Q[0] == A[0]:
        Q.popleft()
        A.popleft()
    else:
        if (len(Q)//2) >= Q.index(A[0]):
            Q.rotate(-1)
            cnt += 1
        else:
            Q.rotate(1)
            cnt += 1
print(cnt)