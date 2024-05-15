def fibonacci_vong_lap(n): #fibonacci vòng lặp
    f = 0
    f1 = 0 
    f2 = 1
    if n == 0:
        return n
    else:
        for i in range(2, n + 1):
            f = f1 + f2
            f1, f2 = f2, f
        return f
    
def fibonacci_de_quy(n): #fibonacci vòng lặp
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

n = int(input("Nhap vao n: "))

print(f"fibonacci_vong_lap({n}) = {fibonacci_vong_lap(n)}")
print(f"fibonacci_de_quy({n}) = {fibonacci_de_quy(n)}")