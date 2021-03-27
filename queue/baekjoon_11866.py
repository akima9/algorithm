# N,K = map(int,input().split())
# A = [i for i in range(1,N+1)]
# idx = 0

# print('<',end='')
# while A:
#     idx += (K-1)
#     while idx >= len(A):
#         idx -= len(A)
#     print(A.pop(idx),end='')
#     if A:
#         print(',',end=' ')
# print('>',end='')

from collections import deque

N,K = map(int,input().split())
A = deque([i for i in range(1,N+1)])

print('<',end='')
while A:
    A.rotate(-(K-1))
    print(A.popleft(),end='')
    if A:
        print(',',end=' ')
print('>',end='')