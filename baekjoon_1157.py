a = str(input()).upper()
b = set(a)
tempCnt = 0
for i in b:
    cnt = a.count(i)
    if tempCnt < cnt:
        tempCnt = cnt
        temp = i
    elif tempCnt == cnt:
        temp = '?'
print(temp)