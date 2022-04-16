# pure recursion without memoisation
# it is still quick for factorial calculation

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
    
print(factorial_function(30))
