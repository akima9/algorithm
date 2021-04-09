n = int(input())
score = list(map(int,input().split()))
maxScore = max(score)
sumScore = 0
for i in score:
    sumScore += (i / maxScore) * 100
print(sumScore / n)