"""
#-------------complex number --------------
#----operation allowed in complex   -----


z = 3 + 4j
print(z,type(z))
print(z.real,z.imag)

x= 0b1111 +4j
print(x,type(x))

y=z+x
print(y)


#---------------boolean data type   (True and False )--------------

a = True 
B = False

print(a+a+a+a)
print(B)
print(a+B)

#--------------size of data type -----------

import sys
a=10
b=10.00023
c="anshu"
d=True
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))

#-----------reference variable  -------------

a=20
b=20
c=30
print(id(a))
print(id(b))
print(id(c))


"""
# -------------- type casting -----------------

# ------------implicit--------
a=10
b=10.5
c=a+b
print(a,type(a))

print(c,type(c))

#-----------------explicit ---------------

b= int(a)
print(b,type(b))

a=int(float("10.76"))
print(a,type(a))

try:
   b=2+0j
   a=float(b)
   print(a,type(a))
except Exception as e:
    print(e)

