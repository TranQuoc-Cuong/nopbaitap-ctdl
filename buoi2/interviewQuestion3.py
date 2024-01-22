def printUnorderedPair(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(str(array[i])+","+str(array[j]))

printUnorderedPair([1,2,3])