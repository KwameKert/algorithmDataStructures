def selectionSort(args):

    currentIdx = 0

    while currentIdx < len(args) -1:
        smallestIdx = currentIdx

        for i in range(currentIdx+1, len(args)):

            if args[smallestIdx] > args[i]:
                smallestIdx = i

        swap(currentIdx, smallestIdx, args)
        currentIdx += 1

    return args



def swap(i, j, args):

    args[i], args[j] = args[j], args[i]


