####  4.1.1.13 LAB Closures and Decorators

## Closures DECLARATION:

def f1(param1):
    param2 = param1  # local parameter not accessibe from outside

    def f2():
        return param2
    return f2			# f2 called WITHOUT ()!
 
## Closures USAGE

f1("Return this text")()  # EXTRA () NEEDED!


  
#### Decorators - add extra options to existing function:
## Declaration:

def f1(exist_function):

    def f2(exist_function_params):
        print("This is extra text added")
	      ## NOW RUN EXIST FUNCTION INSIDE HERE
	      return exist_function(exist_function_params)
	
    return f2           # NO PARENTASIS (). We dont call f2 here!!
  
  
## Decorators Usage:

@f1                      # Decorator initiation
def some_function(x):
    print(x)
  
print("This is from function)

## As the result there will be 2 lines:
## > This is extra text added
## > This is from function
 
 

