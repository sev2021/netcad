fib_list = [1,1]  # memoisation

def fib_fun(n):
    if n < len(fib_list): # reading instead of re-calculating
        return fib_list[n]
    new_fib = fib_fun(n-1) + fib_fun(n-2)
    fib_list.append(new_fib)
    return new_fib

# TESTING

print(fib_fun(14))
print(fib_fun(15))
print(fib_fun(16))
print(fib_fun(17))
print(fib_fun(18))

# Memoisation output

print(fib_list)
