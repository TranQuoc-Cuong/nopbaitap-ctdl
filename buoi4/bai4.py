def kt_dao_chu(chuoi_1, chuoi_2):
    for i in range(len(chuoi_1)):
        check = False
        for j in range(len(chuoi_2)):
            if chuoi_1[i] == chuoi_2[j]:
                check = True
                break
        if not check:
            return False
    return True

chuoi_1 = "restful"
chuoi_2 = "fluster"

print(str(kt_dao_chu(chuoi_1, chuoi_2)))
