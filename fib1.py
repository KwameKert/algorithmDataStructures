#fibonacci series . Recursive approach
#math formular : fib(n) = fib(n-1) + fib(n-2)
#Time complexity 2^n






def fib(n):
    if n ==  2:
        return 1;
    elif n == 1:
        return 0;

    return fib(n-1) + fib(n-2);



print(fib(3))
