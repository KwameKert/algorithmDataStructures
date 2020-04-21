#bubble sort implementation.
#loop through each element comparing if its in order with the next element.

def bubbleSort(args):

    isSorted = False
    counter = 0

    while not isSorted:
        isSorted = True
        for idx in range(len(args) -1 -counter):

            if args[idx] > args[idx+1]:
                swap(idx, idx +1, args)
                isSorted = False

        counter += 1

    return args


def swap(i, j, args):

     args[i], args[j] = args[j], args[i]


#print(bubbleSort([9, 4, 2, 0, 89, 90, 70]));
