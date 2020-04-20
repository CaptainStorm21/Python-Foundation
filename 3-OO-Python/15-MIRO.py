#method resolution order

class A:
    num = 10
    
class B(A):
    pass

class C(A):
    num = 1
    
class D(B, C):
    pass 

print (D.num)
#output 1

print(D.mro())

# A shares data with B and C
# B and C shares data with D