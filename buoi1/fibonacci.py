def fibonacci(x):
    assert x >= 0 and int(x) == x
    if x in [0, 1]:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
    
x = int(input("nhap n: "))
print(int(fibonacci(x)))
