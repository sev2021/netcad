####  4.1.1.13 LAB Closures and Decorators

## Closures DECLARATION:

def f1(param1):
    param2 = param1  # local parameter not accessibe from outside

    def f2():
        return param2
    return f2			# f2 called WITHOUT ()!
 
## Closures USAGE

f1("Return this text")()  # EXTRA () NEEDED!


  
#### Decorators - add extra options to external function:
## Declaration:

def decorator(f3_function):

    def wrapper(f3_params):
        print("This is extra text added")
	      ## NOW RUN EXTERNAL FUNCTION INSIDE HERE
	      return f3_function(f3_params)
	
    return wrapper           # NO PARENTASIS (). We dont call f2 here!!
  
  
## Decorators Usage:

@decorator                    # Decorator initiation
def external_function(x):
    print(x)
  
external_function("This is from function")

## As the result there will be 2 lines:
## > This is extra text added
## > This is from function

##  Short decorator use:

def external_function(x):
    print(x)

decorator(external_function)("This is from function")  # REMEMBER TWO PAIR OF BRAKETS!!!

 
 

