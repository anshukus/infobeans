#--------------day 6 ----------

"""i=1
while i<=20:
    print(i)
    if i==15:
        print("tel khatam hai ")
        break
    i +=1


for i in range(20):
    print(i)
    if i==15:
        print("tel khatam hai ")
        break
   

while True:
     password =input ("enter password ")
     if password == "admin":
         print("access granted ")
         break
     else:
         print("fir se likho")"""


"""n= int(input("enter the number "))
if n<=1:
   print("not prime")
else: 
  x=0

  i=2
  while i<n:
     if n%i == 0:
        x=1
        break
     i +=1
  if x == 0:
     print("prime")
  else:
     print("not prime")


#--------optimize version----------
     
n= int(input("enter the number "))
if n<=1:
   print("not prime")
else: 
  x=0

  i=2
  while i<=n//2:
     if n%i == 0:
        x=1
        break
     i +=1
  if x == 0:
     print("prime")
  else:
     print("not prime")




import math
n= int(input("enter the number "))
if n<=1:
   print("not prime")
else: 
  x=0

  i=2
  while i<=int(math.sqrt(n)):
     if n%i == 0:
        x=1
        break
     i +=1
  if x == 0:
     print("prime")
  else:
     print("not prime")"""



"""n = int (input("enter the number "))
for i in range(1,11):
     if n*i >50:
        break
     print(n*i)

n = int (input("enter the number "))
for i in range(1,11):
     if n*i ==50:
        continue
     print(n*i)"""

i=0
while i<10:
   i +=1
   if i%2==0:
     continue
   print(i)
   

for i in range(1,11):
    if i%2==0:
        continue
    print(i)

        

try:

 while True:
    n= int (input("enter the number :"))
    if n<0:
        continue
    elif  n== 10:
        break
    else:
        print("enter the number again :")
 print("out of the loop")

except Exception as e:
     print(e)
