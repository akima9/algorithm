a = input()
strArr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in strArr:
    a = a.replace(i, '+')
print(len(a))