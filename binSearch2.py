#Binary Search using the iterative approach
#Time O(log(n))  | Space O(1)

def binSearch(array, target):

    left = 0
    right = len(array)-1
    middle = (left+ right)//2

    while left < right:

        if array[middle] == target:
            return middle

        elif target < array[middle]:
            right = middle -1

        else:
            left = middle +1


    return -1;




result = binSearch([1,2,3,4,5],3)
print(result)

