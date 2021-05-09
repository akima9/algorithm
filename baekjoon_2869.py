import math
A = list(map(int,input().split()))

X = (A[2] - A[0]) / (A[0] - A[1]) + 1

print(math.ceil(X))