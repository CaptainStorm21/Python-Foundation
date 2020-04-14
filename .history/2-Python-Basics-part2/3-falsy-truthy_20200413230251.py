#truthy and fallsey

# output - true
print(bool('Hello'))

# output - true
print(bool(5))

# output - false
print(bool(''))

# output - false
print(bool(0))


Falsey
None
Fase
0
0.0
0j
Decimal(0)
Fraction(0,1)
[] - empty array
{} - empty dict
() - empty tuple
'' - empty string
b'' - empty byte
empty range like range(0)
obj.__bool