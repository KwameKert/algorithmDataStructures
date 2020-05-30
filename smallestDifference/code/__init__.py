
#finding the smallest difference from two arrays

def smallestDifference(firstList, secondList):
    #sort arrays
    firstList.sort()
    secondList.sort()

    #pointers
    firstPointer= 0
    secondPointer = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while firstPointer < len(firstList) and secondPointer < len(secondList):
        #getting value from each array
        firstNumber = firstList[firstPointer]
        secondNumber = secondList[secondPointer]

        #get current value
        current = abs(firstNumber - secondNumber)

        #if first item less than second item increase firstPointer else do otherwise
        if firstNumber < secondNumber:
            firstPointer += 1
        elif firstNumber > secondNumber:
            secondPointer +=1
        else:
            return [firstNumber, secondNumber]

        #recalculate the value of smallest
        if smallest > current:
            smallest = current
            smallestPair = [firstNumber , secondNumber]

    return smallestPair


#RESULT = smallestDifference([3, 2, -1, 0, 5], [4, -2, 7, -9])
#print(RESULT)
