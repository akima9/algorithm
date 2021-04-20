a = input()
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cnt = 0
for i in a:
    for k in dial:
        if i in k:
            cnt += dial.index(k) + 3
print(cnt)