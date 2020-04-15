#Finding the product sum of the following array


def productSum(array, maxDepth=1):

    sum = 0
    for item in array:
        if type(item) is list:
           sum += productSum(item, maxDepth+1)
        else:
            sum += item;

    return sum*maxDepth;




#result = productSum([5,2,[7,-1],3,[6,[-13,8],4]])
#result = productSum([1,2,[2,3,3],3,4,5])
#print(result)


