def threeNumber(args, target):
    result = []
    #loop through array
    for i in range(len(args) -2):
        #pointers left and right
        left = 1;
        right = len(args) -1

        #check if current item + args[left] + args[right] equal target
        while(left< right):
            currentSum = args[i] + args[left] +args[right]

            if currentSum == target:
                result.append([args[i], args[left], args[right]])
                left += 1
                right -= 1
            elif currentSum <  target:
                left += 1
            elif currentSum > target:
                right -= 1

    return result



