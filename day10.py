""" -------------: nested loop :--------------
placing loops in another loop 

--------------:   nested while loop  :------------

initialization

while condition 1 :
        statement 1
        initialization 
        while condition 2 :
                 statement 2
                 increment/decrement
        increment/decrement

print("out of both loop")


"""

"""
student=int(input("enter the number of student :"))
subjects= int(input ("enter the number of subjects :"))
chapters= int(input ("enter the number of chapters :"))

i=1
j=1
k=1
while i <= student:
     print("student =",i)
     print("\n")
     i+=1
    
     while j <= subjects:
          print("subject =",j)
          print("\n")
          j+=1
          
          while k <=chapters :
                         print("chapter =",j)
                         print("\n")
                         k +=1
         
"""


"""---------------: nested for loop  :--------------- 
syntax :-

for i in range(rows):
     body of outer

     for j in range(columns):
             statement inside inner

"""

"""

student=int(input("enter the number of student :"))
subjects= int(input ("enter the number of subjects :"))
chapters= int(input ("enter the number of chapters :"))

for j in range(1,subjects+1):
          print("subjects =",j)
          print("\n")
          for k in range(1,chapters+1):
              print("chapters =",k)
              print("\n")

"""

#-------------: combined nested loop  :----------

"""

student=int(input("enter the number of student :"))
subjects= int(input ("enter the number of subjects :"))
chapters= int(input ("enter the number of chapters :"))

i=1
while i <= student:
     print("student =",i)
     print("\n")
     for j in range(1,subjects+1):
          print("subjects =",j)
          print("\n")
          for k in range(1,chapters+1):
              print("chapters =",k)
     print("\n")
     i+=1
print("out of loop :")


"""

#  --- write a program to print prime number between two numbers  ---

num1= int(input ("enter the number1 :"))
num2= int(input ("enter the number2 :"))

for i in range(num1,num2+1):

                         
                         if i==1:
                                print(i," not prime number \n")
                                break
                         elif i == 2:
                                print(i,"prime number \n")
                                continue
                         else:
                             count=0
                             for j in range(1,i//2):
                                 if i%j==0:
                                       if count>2:
                                           break
                                       else:
                                           count +=1
                                 else:
                                       continue
                             if count == 1:
                                    print(i," = prime number \n")
                             else:
                                    print(i," = not prime \n")

    


"""

x=int(input("enter f n 1:"))
y=int(input("enter f n 2:"))

for i in range(x,y+1):
         temp = n
         power =len(str(n))
         total =0
         while temp >0:
                 digit=temp%10
                 total = total +digit**power
                 temp = temp//10
         if  total ==n:
                  print(n)

"""


x=int(input("enter f n 1:"))
y=int(input("enter f n 2:"))

for i in range(x,y+1):
        j=1
        print("\n")
        while j<=10:
               print(i,"x",j,"=",i*j)
               j +=1















