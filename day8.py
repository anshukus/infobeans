print("----------  Day 8 of coding  -------------")


print("------------membership operators ------------")


print("---------- in operator ----------")

name= "python"
print("p" in name)
print("on" in name)

marks = [30,50,70,60]



print("---------- not in operator ----------")

name= "python"
print("Py" not in name)
print("py" not in name)



print(""" ------------- identity operator ----------
:-
 used to compare the objects both objects are same data type and share same memory location there are different identity operator available.


*1:-( is )- it check if tow variables points to the same object (same memory location)

*2:- (is not ) it is the opposite of is if two variables point to different objects then it returns true otherwise it return false .


the euality operator is used to comapare the value of two variable

where the identity operator used to compare memory location of two variable



""")


a=10
b=10

print(a is b)
print(a==b)

a=[10,20]
b=[10,20]

print(a is b )
print(a==b)


print("""----------- bitwise operator ---------------
python bitwise operator are used to performe bit wise calculation on integers the integers are first converted into binary and then operaton are perform on each bit the result is return in decimal format 

operators :-

& :- bitwise and 
| :- bitwise or
^ :- bitwise xor
<< :- bitwise left shift
>> :- bitwise right shift
~ :- bitwise one's compliment ( bitwise not )


a   b     a&b   a|b   a^b

0   0      0     0     0
1   0      0     1     1
0   1      0     1     1
1   1      1     1     0



""")


a=5
b=6
print(a&b)  # first it converted into binary then operator 
print(a|b)
print(a^b)

print("\n\n" )
a=9 
b=11

print(a&b)  # first it converted into binary then operator 
print(a|b)
print(a^b)


print(""" ----------- bitwise left shift operator (<<)------------

in bitwise left shift operator toward from left side n number of bits  need to be droped  toward from right side empty places need to be filled with zeros.

ex :-
a=5
print(a<<1)
5- remove (0)000 0000 0101(add 0)
       get 0000 0000 1010

""")

a=5
print(a<<1)

a=3
print(a<<1)

a=19
print(a<<1)


print(""" ----------- bitwise one's compliment ---------

:- In bitwise one's compliment all one's will be converted in to zero's and all zero's will be one's   it perfomes bitwise negation .

**add 1 in the number and - laga do 

""")

a=4
print(~a)
print(~~a)
print(a+1)

print(""" ----------- bitwise right shift operator (<<)------------

in bitwise right shift operator toward from right side n number of bits  need to be droped  toward from left side empty places need to be filled with zeros.

ex :-
a=5
print(a>>1)
5- (add 0)000 0000 010(1 remove )
       get 00000 0000 10

""")

a=5
print(a>>1)
a=11
print(a>>1)

a=-11
print(a>>1)

a=-33
print(a>>1)

a=-7
print(a>>1)

a=-9
print(~a)


n= int(input("enter the number :"))

if 1&n == 1:
   print("odd")
else:
   print("even")

a=10
b=20
a=a^b
b=a^b
a=a^b
print(a)
print(b)




