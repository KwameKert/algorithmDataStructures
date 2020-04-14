#Binary search using the recursive approach


def binSearch(array, target):

    return binSearchHelper(array,target, left= 0,right = len(array)-1)


def binSearchHelper(array,target,left,right):
    if left > right:
        return -1

    middle = (left +right)//2
    potentialValue = array[middle]

    if target == potentialValue:
        return middle

    elif target < potentialValue:
        binSearchHelper(array,target,left, middle -1)
    else:
        binSearchHelper(array, target,middle+1,right)


result = binSearch([1,2,4,8,9],4)

print(result)
