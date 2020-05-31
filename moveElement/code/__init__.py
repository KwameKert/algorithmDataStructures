#moving element to end of array


def moveElement(args, target):

    left = 0
    right = len(args) -1

    while left <  right:
        leftItem = args[left]
        rightItem = args[right]

      # if increase right if rightItem is equal to targe
        if rightItem == target:
            right -= 1
      # if left item is equal to target swap values with right and increase left value
        elif leftItem == target:
            #swap elements
            args[left], args[right] = args[right], args[left]
            left += 1

        else:
           left +=1

    return args


#RESULT = moveElement([2, 1, 2, 2, 2, 2, 3, 4, 5, 2], 2)
#print(RESULT)
