def Neper(n):
    def giaithua(k):
        if k == 0 or k == 1:
            return 1
        else:
            return k * giaithua(k-1)
    
    e_sum = sum(1/giaithua(k) for k in range(n+1))
    return e_sum

n = int(input())
print("ket qua:", Neper(n))