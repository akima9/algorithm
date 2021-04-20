#arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라는 말입니다.
# 만약 A가 None 이라면, 처음부터 라는 뜻이고
# B가 None 이라면, 할 수 있는 데까지 (C가 양수라면 마지막 index까지, C가 음수라면 첫 index까지가 되겠습니다.)라는 뜻입니다.
# 마지막으로 C가 None 이라면 한 칸 간격으로 라는 뜻입니다.

a,b = input().split()
a = a[::-1]
b = b[::-1]
if int(a) > int(b):
    print(a)
else:
    print(b)