cache = [1,1]  # cache for memoisation

def factorial_function(n):
    if n < len(cache):
        return cache[n]
    cache.append(n * factorial_function(n - 1))
    return cache[n]
    
print(factorial_function(5))
print(factorial_function(6))
print(factorial_function(7))

print(cache)
