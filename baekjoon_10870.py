n = int(input())

def fibonachi(num):
    if num == 0:
        return 0
    elif num > 0 and num <= 2:
        return 1
    else:
        return fibonachi(num-1) + fibonachi(num-2)

print(fibonachi(n))