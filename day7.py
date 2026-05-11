#----------- Day 7 -------------

"""s = input("enter the string :")
for ch in s:
   if ch in "aeiouAEIOU":
       continue
   print(ch,end="")   
 
print("\n")

s = input("enter the string :").lower()
for ch in s:
   if ch in "aeiou":
       continue
   print(ch,end="")  """


# write a program to skip even numbers stop at 9 and do nothing for 5

"""for i in range(1,11):
     if i==5:
        pass
     elif i==9:
         break
     elif i%2==0:
         continue
     else:
       print(i)"""



#---------- For else ----------


""" In pyhton a for loop can have an optional else block in other programing language they use of else  only with if but python allow else condition with loops.
  
**the else block after for loop is executed only when the loop is not termineted by a break statment  if the loop is termineted by the break the else block will skip.



**loop pura chalega to else print hoga or agar loop bich me kahi break hua to else nahi chalega** """


"""-------- syntax ---------
for variable in sequence:
     loop body
     if condition:
          break
else: 
    print("statments for no break")"""



"""count=1
for i in range(1,50):
     print(i)
     count +=1
     if count==25:
         break
else:
     print("no break")



n = int(input("enter the number :"))

if n<=1:
    print("not prime")
else: 
    for i in range(2,n):
           if n%i ==0:
                print("not prime",n)
                break

    else:
          print("prime",n)


lst=[1,23,4,57,8,6,90,7,5,43,2]
target=6

for i in lst:
   if i== target:
       print ("banda mil gaya")
       break
else:
    print("banda nahi mila")"""



""" advantages  of --------for else------
* cleaner code for searching problem.-: insted of using a separet flag variable to check condition was mat or not for else can be use.
* logical clarity -:
* useful in prime number checking.   """


""" ----------- while else -------------

syntax :-
  
while condition:
      loop body
      if condition:
           break
else:
      execute when break will not come in action   """
try:

  attempts=0
  while attempts<3:
     pass=input("enter password ")
     if the pass == "admin":
           print("access granted")
           break
     attempts +=1
  else:
     print("you have the maximum limit of failed attempts")
except Exception as e:
     print(e)           
  


s = input("enter the string :")
for ch in s:
   if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
       continue
   print(ch,end="")   
 
print("\n")


