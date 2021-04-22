A = list(map(int,input().split()))
if A[1] >= A[2]:
    print(-1)
else:
    result = (A[0] // (A[2] - A[1])) + 1
    print(result)