def twoNumber(args, target):

    #dictionary of existing items
    holder = {}
    #looping through args
    for idx, item in enumerate(args):
        val = target - args[idx]

        #if val in holder return val and current item
        if val in holder:
            return [val, args[idx]]
        else:
            holder[args[idx]] = idx
    return None

