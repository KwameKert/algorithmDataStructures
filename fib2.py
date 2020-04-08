#Recursive Approach implementing memoization
# Time Complexity O(n) Space complexity O(n)

def fib(n, memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]

    else :
        memoize[n] = fib(n-1,memoize) + fib(n-2, memoize)
        return memoize[n]

fib(9)


