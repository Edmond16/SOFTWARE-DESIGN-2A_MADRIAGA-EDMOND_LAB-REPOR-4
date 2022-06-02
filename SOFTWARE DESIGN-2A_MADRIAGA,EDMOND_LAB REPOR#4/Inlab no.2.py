def  product(a,b):
       if b == 1:
              return a
       else:
              return a + product(a, b-1)
test = product(2,3)
print(test)
