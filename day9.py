print(""" ----------- turnary operator----------------
it is also called inline if it allowe writing if else in a single line the turnary operator in python perform conditional checks on assign values or execute expression in a single line""")

"""
#x= value if condtion else value
print("\n")
# if conditon true then return value 1 otherwise value 2
x =30 if 10<20 else 40 
print(x)
print("\n")

n = int(input("enter the value :"))
if n%2==0:
     res="even"
else: 
  res="odd"
print(res)


#------ in turnary operator form 
n = int (input("enter the value :"))
res = "even" if n%2==0  else "odd"
print(res)

print("\n")

a = int (input("enter the value1 :"))
b = int (input("enter the value2 :"))

max = a if a>b else b
print(max)

print("\n")

a = int (input("enter the value1 :"))
b = int (input("enter the value2 :"))

print(f"{a} is greater ") if a>b else print(f"{b} is greater ")

# ------- when all conditions are false then last else will execute-----

res = 10 if 200<30  else 40 if 50<60 else 70
print(res) """


a= 100
b= 200
c= 30

max =a if a>b and a>c else b if b>c else c
print(f"{max} is greater")

a= 100
b= 200
c= 30
print("equal" if a==b else "greater" if a>b else "small" )


""" --------: advanteges of turnary operator :--------

* concise : reduce the code length.
*readable code :  it immedetily show condition and results.
*suppose inline decisions : no need to  break code into multiple lines.
"""

i=1
while i<=10:
  print(i, "even" if i%2==0 else "odd")
  i=i+1

"""------------: python match case condition :----------
it is introduce in python 3.10 it allow us to perform more readable contional checks it is used to create menu driven programs.

syntax :

match variable:
   case pattern1:
       code block1
   case pattern2:
       code block 2
   ---------
   ---------
   case __:
        default block

"""
"""a= int (input("enter choice :"))
match  a:
   case 1:
    print("one")
   case 2:
    print("two")
   case 3:
    print("third")

   case _:
     print("wrong choice ")


a= int (input("enter choice :"))
if  a==1:
   print("one")
elif  a==2:
   print("two")
elif  a==3:
   print("third")
elif  a==4:
   print("four")
else:
   print("wrong choice")"""




"""
a= int (input("enter choice :"))
match  a:

   case 2:
    print("two")
   case 3:
    print("third")
   case 1:
    print("one")

   case _:
     print("wrong choice ")
print("out of match case")"""


#--------------: default case is not nessesary  :-----------

#------- two case can be same but run only first case and also we can put many choices in one case  ----------

"""a= int (input("enter choice :"))
match  a:

   case 2:             #------- two case can be same but run only first case
    print("two")
   case 2:             #------- two case can be same but run only first case
    print("third")
   case 1|3|4|5:       #------- we can put many choices in one case  ----------

    print("one")

   case _:
     print("wrong choice ")
print("out of match case")"""


"""
a= int (input("enter choice 1 to 5 :"))

match  a%2:     # ---------- match case can be expression --------

   case 2:
    print("two")
   case 2:
    print("third")
   case 1|3|4|5:
    print("one")

   case _:
     print("wrong choice ")
print("out of match case")


day= input("enter choice 1 to 5 :")

match  day:     # ---------- match case can be string --------

   case 'monday':
    print("two")
   case 'tuesday':
    print("third")
   case 'wednesday':
    print("one")

   case _:
     print("wrong choice ")
print("out of match case")          """


while True:
   try:
       ch= int (input("enter 0 to termiate the task otherwise enter any number :"))
       if ch==0:
            break
       else:
            a= int (input("enter number 1 :"))
            b= int (input("enter number 2 :"))

            opt = input ("entre operator :")

            match opt:
                  case "+":
                      print("addition =",a+b)
                  case '-':
                      print("subtraction =",a-b)
                  case '*':
                      print("multiplication =",a*b)
                  case '/':
                      if b!=0:
                           print("division =",a/b)
                      else:
                           print("avoid zero ")
                  case '//':
                           if b!=0:
                                   print("addition =",a//b)
                           else:
                                   print("avoid zero ")
                  case _:
                      print("no match case ")

   except Exception as e:
                print("bhadwe aukaat me number daal alphabate nahi ",e)
print("out of match case ")


""" -------------- gurd in match case -------------
* it is an additonal conditon return using if inside a case if allow you to add extra checking logic to a case pattern the case bolck execute only if the pattren matches and the gurd conditon is true .  


"""

age= int (input("enter age :"))



match age:
    case x if x>18 :
        print("adult")

    case x if x>50:
        print("old")

    case x if 0<x<18:
        print("too young")

    case _:
        print("no match case ")

print("out of match case ")




student=int(input("enter the number of student :"))
subjects= int(input ("enter the number of subjects :"))
chapters= int(input ("enter the number of chapters :"))


for i in range(0,student):
     print("student =",i)
     print("\n")
     for j in range(0,subjects):
          print("subjects =",j)
          print("\n")
          for k in range(0,chapters):
              print("chapters =",k)
              print("\n")
print("out of loop ;")








