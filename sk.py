
def aprekini(x):
  import math
  list=[]
  list.append(x%1)
  list.append(math.pow(x,2))
  list.append(math.sqrt(x))
  if x>0:
    list.append(">")
  elif x<0:
    list.append("<")
  else:
    list.append(0)
  return list