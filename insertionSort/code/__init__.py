
def insertionSort(args):

    for i in range(1, len(args)):
        j = i
        while j > 0 and args[j] < args[j-1]:
            swap(j, j-1, args)
            j -= 1


    return args;


def swap(i, j, args):
    args[i], args[j] = args[j], args[i]




