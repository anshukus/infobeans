"""
n1= int(input("enter the number of starting point:"))
n2= int(input("enter the number of endinging point:"))
n3= int(input("enter the number of step :"))
num_of_line=0

for i in range(n1,n2,n3):
          print("\n")
          num_of_line +=1
          for j in range(n1,i+1,n3):
                 print(j,end=" ")
print("\n","number of lines :",num_of_line)  """

"""

8 7 6 5 4 3 2 1
7 6 5 4 3 2 1
6 5 4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1  

"""

"""
n= int(input("enter the n :"))

i = n 

while i>=1:
     print()
     j=i
     while j>=1:
          print(j,end=" ")
          j= j-1
     i=i-1


print("\n")

"""

"""

element = int (input("enter the number "))
for i in range(0,element+1):
         if element%2==0:
             for k in range(1,i+1):
                      print(" ",end='')
             for j in range(element//2 -i):
                      print('*',end='')
             for l in range(1):
                      print(" ",end='')
             for m in range(element//2 -i):
                      print('*',end='')
             print()
         
         else:
             print("you can't create pattern element is not even number")

"""


"""
1 2 3 4 5 6 7 8
2 3 4 5 6 7 8
3 4 5 6 7 8
4 5 6 7 8
5 6 7 8
6 7 8
7 8
8
"""
"""
n= int(input("enter the n :"))

i = 1 
while i<=n:
   print()
   j=i
   while j<=n:
         print(j,end=" ")
         j= j+1
   i= i+1          


"""
""" ----------experiment code :-0 

n= int(input("enter the n :"))

i = n 
while i>=n:
   print()
   j=i
   while j>=n:
         print(j,end=" ")
         j= j-1
   i= i-1     

"""

"""

n1= int(input("enter the number of starting point:"))
n2= int(input("enter the number of endinging point:"))
n3= int(input("enter the number of step :"))
num_of_line=0

for i in range(n1,n2+1,n3):
          print()
          num_of_line +=1
          for j in range(n1,i+1,n3):
                 print(i,end=" ")

print("\n")


"""



"""
2 2 2 2 2 2 2
3 3 3 3 3 3
4 4 4 4 4
5 5 5 5
6 6 6
7 7
8
"""

"""

n= int(input("enter the n :"))

i = 1

while i<=n:
     print()
     j=i
     while j<=n:
          print(i,end=" ")
          j= j+1
     i=i+1


n= int(input("enter the n :"))

i = 1

while i<=n:
   if i%2==0:
     print("*")
     print()
   else:
     j=1
     while j<=i:
          print(i,end=" ")
          j= j+1
     i=i+1




n1= int(input("enter the number of starting point:"))
n2= int(input("enter the number of endinging point:"))
n3= int(input("enter the number of step :"))
num_of_line=0

for i in range(n1,n2,n3):
          print("\n")
          num_of_line +=1
          for j in range(n1,i+1,n3):
                 if j%2==0:
                        print("*",end=" ")
                 else:
                 print(j,end=" ")
print("\n","number of lines :",num_of_line)


"""


"""

n= int(input("enter the number:"))

i= 1
k=1
while i<=n:
    print()
    j=1
    while j<=i:
         print(k,end=" ")
         j= j+1
         k= k+1
    i = i+1

"""


"""

n= int(input("enter the number:"))

i=1
while i<=n:
    print()
    j=1
    while j<=i:
         print(j,end=" ")
         j = j+1
    k=1
    while k <= (n -i):
              print("*",end=" ")
              k =k+1
    

    l= n-i
    while l >=1:
              print("*",end=" ")
              l =l-1
    

    i = i + 1



"""

""" 

n= int(input("enter the number:"))

i=1
while i<=n:
    print()
    j=1
    while j<=n-i:s
         print(" ",end=" ")
         j = j+1
    k=1
    while k <= i:
              print(k,end=" ")
              k =k+1
    
    i = i+1

""" 

n= int(input("enter the number:"))

i=1
while i<=n:
    print()
    j=1
    while j<=n-i:
         print(" ",end=" ")
         j = j+1
    k=1
    ch=65
    while k <= i:
              print(chr(ch),end=" ")
              ch +=1
              k =k+1
    
    i = i+1









