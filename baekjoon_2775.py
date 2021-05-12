testCase = int(input())#테스트케이스

for T in range(testCase):
    floor = int(input()) #층
    room = int(input()) #호
    zeroFloor = [] #0층
    for i in range(1,room+1):
        zeroFloor.append(i)
    
    for k in range(floor):
        for n in range(1,room):
            zeroFloor[n] += zeroFloor[n-1]
    
    print(zeroFloor[-1])