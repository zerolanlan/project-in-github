##  def fact(n):
##  if n==0:
##      return 1
##  else:
##      return n*fact(n-1)
##print(fact(5))
def recursion(n):
    n-=1
    return recursion(n)
print(recursion(5))
