## Example of custom class for calculating Fibonacci numbers
## Based on generator/iterator

class Fibo():
  def __init__(self.n):     ## n-steps of calculation
    self.n = n
    self.f1 = self.f2 = 1   ## ancilary variables
    
  def __iter__(self):       ## __iter__ is requred to initialise iteration
    return self
  
  def __next__(self):       ## __next__ defines way of changing iteration
    self.f1, self.f2 = self.f2, self.f1 + self.f2
    self.n -= 1
    if self.n < 1:
      raise StopIteration
    return self.f1
  
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
  
