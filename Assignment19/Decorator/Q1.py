# Develop a memoization decorator that caches the results of function 
# calls and returns the cached result when the same inputs occur again. 
# This can greatly improve the performance of recursive or 
# computationally intensive functions.

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Returning cached result for", args)
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))
print("Factorial of 6:", factorial(6)) 
