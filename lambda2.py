from functools import reduce
precios=[1,2,3,4]
total= reduce(lambda x, y: x + y,precios)
print(total)