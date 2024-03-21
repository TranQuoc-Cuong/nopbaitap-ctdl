def dequyfib(n):
    if(n <= 1):
        return n
    else: 
        return fib(n - 1) + fib(n - 2)
    
def fib(n): 
    f1 = 0
    f2 = 1

    if(n == 0):
        return f1
    
    elif (n == 1):
        return f2
    
    else:
        for i in range(2, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f2



n = int(input())
print("fn de quy la:", dequyfib(n))
print("fn la:",fib(n))

