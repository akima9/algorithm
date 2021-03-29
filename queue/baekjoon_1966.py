from collections import deque
A = int(input())

for i in range(A):
    cnt = 0
    N,M = map(int,input().split())
    important = deque(list(map(int,input().split())))
    
    while True:    
        if important[0] == max(important):
            if M == 0:
                cnt += 1
                print(cnt)
                break
            else :
                important.popleft()
                cnt += 1
                M -= 1
        else:
            important.rotate(-1)
            if M > 0:
                M -= 1
            else:
                M += len(important) - 1