#Iterative approach ;
#Time complexity of O(n) ; Space Complexity of O(1)


def fib(n):
    lastTwo = [0, 1]
    counter = 3

    while counter <= n:
        nextVal = sum(lastTwo)
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextVal
        counter += 1

    return lastTwo[1] if n > 1 else lastTwo[0]

print(fib(9))
