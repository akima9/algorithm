N = int(input())
temp = N
cnt = 0
while True:
    left = temp // 10
    right = temp % 10
    temp = left + right
    temp = int(str(right) + str(temp % 10))
    cnt += 1
    if N == temp:
        break
print(cnt)
