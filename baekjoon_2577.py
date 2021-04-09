mulNum = 1
for i in range(3):
    inNum = int(input())
    mulNum *= inNum
a = list(str(mulNum))
for j in range(10):
    print(a.count(str(j)))