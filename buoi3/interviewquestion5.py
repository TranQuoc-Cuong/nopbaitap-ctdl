def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 10000):
                print(str(arrayA[i])+","+str(arrayB[j]))

manga = [1,2,3]
mangb = [3,2,1]
printUnorderedPairs(manga, mangb)