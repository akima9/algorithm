N = int(input())
A = 1
cnt = 1
if N != 1:
    while True:
        A += 6 * cnt
        cnt += 1
        if N <= A:
            break
print(cnt)