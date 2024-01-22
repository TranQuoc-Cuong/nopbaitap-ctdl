def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000): 
                if arrayA[i] < arrayB[i]:
                    print(str(arrayA[i])+","+str(arrayB[j]))
                    break

printUnorderedPairs([1,2,3], [3,2,1])