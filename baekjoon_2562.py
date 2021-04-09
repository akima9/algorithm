a = []
for i in range(9):
    a.append(int(input()))
maxNum = max(a)
print(maxNum)
print(a.index(maxNum) + 1)
