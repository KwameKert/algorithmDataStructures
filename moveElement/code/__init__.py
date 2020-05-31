#moving element to end of array


def moveElement(args, target):

    left = 0
    right = len(args) -1

    while left <  right:
        leftItem = args[left]
        rightItem = args[right]

        #return
        if rightItem == target:
            print("right item", right)
            right -= 1
        elif leftItem == target:
            #swap elements
            args[left], args[right] = args[right], args[left]
            print(args)
            left += 1

        else:
           left +=1

    return args


RESULT = moveElement([2, 1, 2, 2, 2, 2, 3, 4, 5, 2], 2)
print(RESULT)
