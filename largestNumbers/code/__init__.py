#Naive approach

#def largestThreeNumbers(args):
#    args.sort()
#    result = args[-3:]
#    return result



#Optimized approach

def largestThreeNumbers(args):

    threeNumbers = [None, None, None ]

    for num in args:
        updateNumbers(threeNumbers, num)

    return threeNumbers;


def updateNumbers(threeNumbers, num):

    if threeNumbers[2] is None  or num > threeNumbers[2]:
        updateAndShift(threeNumbers, num, 2)

    elif threeNumbers[1] is None  or num > threeNumbers[1]:
        updateAndShift(threeNumbers, num , 1)

    elif threeNumbers[0] is None  or num > threeNumbers[0]:
        updateAndShift(threeNumbers, num , 0)


def updateAndShift(array, num, idx):

    for i in range(idx +1):

        if i == idx:
            array[i] = num

        else:
            array[i] = array[i +1]



numbers = largestThreeNumbers([10, 32, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(numbers)
