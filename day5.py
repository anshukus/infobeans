a=256
b=256

print(id(a))
print(id(b))
print(a is b)

a=260
b=260

print(id(a))
print(id(b))
print(a is b)

a=int('256')
b=int('256')


print(id(a))
print(id(b))
print(a is b)

a=int('260')
b=int('260')


print(id(a))
print(id(b))
print(a is b)

a="bahu"*3
print(a)

# ------------assignment operator --------------
# assign value left side variable to right side value

a=10 
a-=5
print(a)

a=b=c=d=10
print(a,b,c,d)

a=5
b=2
a+=b*3
print(a,b)

a=17
a//=3+1  # first addition then floor division
print(a)


#------------relational operator -------------
a=5
b=5.0
print(id(a),id(b))
  
#ord() use for getting uni code of single character----
print(ord('a'))

a="Anshu"
b="anshu"
print(a>b)









