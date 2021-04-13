def d(n):
    this = n
    for i in str(n):
        this += int(i)
    return this

a = set(i for i in range(1,10001))
b = set()
for i in range(1,10001):
    b.add(d(i))

result = sorted(a - b)
for i in result:
    print(i)
