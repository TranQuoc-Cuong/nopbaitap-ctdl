def printUnorderedParirs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i])+","+str(arrayB[j]))

printUnorderedParirs([1,2,3],[3,2,1])