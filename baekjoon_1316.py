N = int(input())
cnt = 0
for i in range(N):
    word = input()
    print(sorted(word,key=word.find))
    if list(word) == sorted(word,key=word.find):
        cnt += 1
print(cnt)