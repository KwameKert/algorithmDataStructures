
#finding the smallest difference from two arrays

def smallestDifference(firstList, secondList):
    #sorting both arrays
    firstList.sort()
    secondList.sort()

    smallestPair = []
    idxOne = 0
    idxTwo = 0

    current = float("inf")
    smallest = float("inf")

    #loop through both arrays till the end of its range
    while idxOne < len(firstList) and idxTwo < len(secondList):
        firstNumber = firstList[idxOne]
        secondNumber = secondList[idxTwo]

        current = abs(firstNumber - secondNumber)

        if firstNumber < secondNumber:
            idxOne += 1
        elif firstNumber > secondNumber:
            idxTwo += 1
        else:
            return [firstNumber, secondNumber]

        if smallest > current:
            smallest = current
            smallestPair = [firstNumber, secondNumber]

    return smallestPair
