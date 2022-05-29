def fib(a):
    if a<=1:
        return a
    return fib(a-1)+fib(a-2)
n=int(input())
for i in range(n):
    print(fib(i),end=" ")