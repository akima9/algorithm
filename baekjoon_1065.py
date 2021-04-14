N = input()

def hansuCheck(N):
    
    cnt = 0
    for i in range(1,int(N)+1):
        if i > 99:
            temp = list(int(j) for j in str(i))
            if temp[0] - temp[1] == temp[1] - temp[2]:
                cnt += 1
        else:
            cnt += 1
    
    return cnt

print(hansuCheck(N))