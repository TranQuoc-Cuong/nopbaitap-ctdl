def Pascal(n):
    tamgiac = [[1]]  # hàng đầu luôn chưa 1 phần tử 1

    for i in range(1, n + 1):
        dong = [1]  # Mỗi hàng bắt đầu bằng số 1
        for j in range(1, i):
            dong.append(tamgiac[i - 1][j - 1] + tamgiac[i - 1][j]) #Thêm phần từ mới bằng cộng hai phần tử phía trên
        dong.append(1)  # Kết thúc mỗi hàng bằng số 1
        tamgiac.append(dong)  # Thêm hàng mới vào tam giác

    for i in range(n + 1):
        print(f'n={i}', end=' ')
        for j in range(i + 1):
            print(tamgiac[i][j], end=' ')
        print()  

n = int(input("Nhap vao n: "))

print(f"Pascal({n}):")
Pascal(n)