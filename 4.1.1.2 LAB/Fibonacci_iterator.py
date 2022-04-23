## Example of custom class for calculating Fibonacci numbers
## Based on generator/iterator

class Fibo():
  ## Fibonacci numbers using iterable class
  
  def __init__(self.n):     ## n-steps of calculation
    self.__n = n
    self.__f1 = self.__f2 = 1   ## ancilary variables
    
  def __iter__(self):       ## __iter__ is requred to initialise iteration
    return self
  
  def __next__(self):       ## __next__ defines way of changing iteration
    self.__f1, self.__f2 = self.__f2, self.__f1 + self.__f2
    self.__n -= 1
    if self.__n < 1:
      raise StopIteration   ## to stop iteration MUST USE exception
    return self.__f1        ## return calculated value
  
  ## call Fib() in iteration:
  for i in Fibo(12):
    print(i)
  
  # return:
  # 1
  # 2
  # 3
  # 5
  # 8
  # 13
  # 21
  # 34
  
  
  ## call usinf generator methond NEXT()
  f = Fibo(12):
  
  next(f)
  
