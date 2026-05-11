a,b,c=10,-10,111
print("A",a,"\nB",b,"\nC",c)
print(type(a),type(b),type(c))

#------binary---- base 2 by 0b or 0B

a=0b1011
b=0B1111
c=-0b1111
print(a,b,c)
print(type(a),type(b),type(c))


#-----octal----  base 8 by 0o or 0O

a=0o137
b=0O137
print(a,b)
print(type(a),type(b))

# ----- hexa decimal-----

# hexa base 16 -----0 to 9 and A B C D E F only  by 0x or 0X

a=0xABC
print(a)
a=0xabc
print(a)

#----base conversion----

"""
bin()
oct()
hex()
"""

print(bin(20))
print(bin(0o137))
print(bin(0xabc))

#-------float-----

x=3.14
y=1.0012
z=0.0

print(x,y,z)

#------------ bin hex oct can not work for float---- 

import math

a=3.7365
print(math.ceil(a))     # round of in up value 3.7=4
print(math.floor(a))    # round of in down value 3.7=3
print(round(a))         # round nearest value 3.7=4  if we want it round value after decimal then we have to spacify like (round(3.7365,2))  =3.74
print(round(a,2))       # if we want it round value after decimal then we have to spacify like (round(3.7365),2)  =3.74

a=1.2e2
print(a)


































