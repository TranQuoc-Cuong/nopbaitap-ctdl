def powersOF2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOF2(int(n/2))
        curr = prev*2
        print(curr)
        return curr

powersOF2(9)