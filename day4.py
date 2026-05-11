#----------boolean-----------

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("anshu"))
print(bool([]))       #  false because list is empty
print(bool({}))
print(bool((1,2,3)))
print(bool(-10))      # everything besides zero is integer thats why true
print(bool(0.00001))
print(bool(1.00322))
print(bool(False))
# for any non empty string boolean function is always true

#--------------complex-------------

print(complex(2))
print(complex(3,4))
print(complex("10"))
print(complex(2.34))


# ------------ python None type ---------------
# there is no null in python there is only None

x = None
print(type(x))
print(None==1)
print(None==False)
print(None==True)
print(None==0)
print(None==None)


#-----------------operators-----------

# ----------------Arithmatic operators ----------------------
# - "" +,-,*,/ =result in float,//=answer in integer ,%= result give remainder,** =power(exponential)""

print(5*6)
print(-5/2)
print(-5//2) # answer is -3 because we use only small value but in negative it will be greater 
print(-5%2)
print(5%-2)
print(-5%-2)
print(-5/2)
print(45%60)  #  45 because numerator is less then denomerator then pick only numerator

x=27
print(x//10)
print(x%10)

print(x**x)
print(5.25%2)
print(9**0.5)
print(16**0.25)

print(x**(1/3))

#----------------precidence and associativity of operator ----------------

x=5+3*4-3
print(x)
print(2**3**2)



 
