def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i])+","+str(arrayB[j]))

mangA = [1,2,3]
mangB = [3,2,1]
printUnorderedPairs(mangA, mangB)