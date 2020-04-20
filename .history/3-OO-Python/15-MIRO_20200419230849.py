#method resolution order

class A:
    num = 10
    
class B(A):
    pass

class C(A):
    num = 1
    
class D(A, C):
    pass 

# A shares data with B and C
# B and C shares data with D