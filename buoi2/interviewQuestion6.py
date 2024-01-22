def reverse(array):
    for i in range(0, int(len(array)/2)):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse([3, 9, 1, 5, 0])