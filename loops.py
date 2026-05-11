print("day :- 6")

print("================while loop=============")
"""i=20
while i>=0:
 print(i)
 i -=3

print("out of loop :")

n=int(input("Enter the number :"))
sum=0
i=1
while i<=n:
   sum=sum+i
   i +=1
print(f"some of n natural number is :{sum}")


n=int(input("Enter the number :"))

i=2
while i<=n:
   print(i,end=" ")
   i +=2
print("even number is")




n=int(input("Enter the number :"))

i=1
while i<=10:
   print(i*n,end=",")
   i +=1
print("out of the loop")"""

"""print("counting of digit in number and addition of digits of number")
n=int(input("Enter the number :"))

sum=0
count=0
while n>0:
   rem=n%10
   sum =sum+rem
   n=n//10
   count +=1
print("sum of digits:",sum)
print("count of digits :",count)"""

"""n=int(input("Enter the number :"))

i=1
while i<=10.5:
   print(i*n,end=",")
   i +=0.1
print("out of the loop")"""


print(" ======== for loop =======")


"""n= input("enter the name :").upper()
x=0
for i in n:
  print(i.lower())
  print("index of ",i ,"is",x)
  x +=1
print(len(n))"""

print("======== for loop in form of range ========")

"""for i in range(3,9,3):
    print(i)


n= int(input("enter number:"))
sum=0

for i in range(n+1):
    sum =sum+i
print(sum)"""

"""n=int(input("enter nummber :"))

for i in range(1,11):
    print(i*n)


for i in range(n,(n*10)+n,n):
    print(i)"""
print("\n \n \n ")

#--------------------24/04/2026----------


#------------------class solution----------------

"""n= int(input("enter number :"))
sum=0
for i in range(2,n+1):
     if i%2==0:
        sum = sum+i
     else:
        pass
print(sum)"""



# -------------perfect number is that number that will be the result of addition of it's divisives-----


"""n= int(input("enter number to check perfect number:"))
sum=0
for i in range(1,(n//2)+1):
    if n%i==0:
       sum= sum+i
    else:
        pass
if sum==n:
   print(f"{n} is a perfect number")
else:
   print(f"{n} isn't a perfect number")



n= int(input("enter number  to check perfect number :"))
sum=0
i=1
while i<=n//2:
    if n%i==0:
       sum= sum+i
    else:
        pass
    i +=1
if sum==n:
      print(f"{n} is a perfect number")
else:
      print(f"{n} isn't a perfect number")

n= int(input("enter number :"))
count=0
for i in str(n):
     count +=1
print("count of the number is : ",count)"""

#-----------reverse of number using for loop-------


"""n= int(input("enter number :"))
rev=0
for i in str(n):
    digit= n%10
    n= n//10
    rev = rev*10+digit
print(rev)"""


#-----------using for loop raw string logic only----------

"""n= input(" for hai with raw string enter number :")
rev=""
for i in n:
    rev=i+rev
    
print(rev)"""

"""n= int(input(" for hai with integer enter number :"))
rev=0
for i in str(n):
    digit= n%10
    print(rem,end="")
    n= n//10
   
print(rev)"""

#-----------reverse of number using while loop-------

"""n= int(input("while hai enter number :"))
rev=0
i=0
while i<n:
   digit= n%10
   n=n//10
   rev=rev*10+digit
print(rev)"""


#---------------palindrome check-----------

"""n= int(input("while hai enter number :"))
rev=0
temp=n
i=0
while i<n:
   digit= n%10
   n=n//10
   rev=rev*10+digit
if rev==temp:
  print(f"number {temp} is palindrome :")
else:
   print(f"number {temp} is not palindrome :")"""


# ----armstrong number problem--------


"""n= int(input("armstrong number with while enter number :"))
am=0
temp=n
i=0
while i<n:
   dig= n%10
   am=dig**3+am
   n=n//10
if am==temp:  
  print(f" {am} is armstrong number ")   
else:
   print("not")"""


try:
 
 n= int(input("armstrong number with while enter number :")
 length=len(str(n))

 am=0
 temp=n
 i=0

 while i<n:

   dig= n%10
   am=dig**length+am
   n=n//10

 if am==temp:  

  print(f" {am} is armstrong number ") 
  
 else:

   print("not")

except Exception as e:

   print(f"your error is {e}")




