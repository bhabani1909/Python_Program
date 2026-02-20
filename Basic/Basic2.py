typecasting
______________
a="10"
b=a
print(type(a),type(b))
print(b*3)


o/p:
<class 'str'> <class 'str'>
101010


string convert to integer
_____________________________

a="10"
b=int(a)
print(type(a),type(b))
print(b*3)

o/p:
<class 'str'> <class 'int'>
30







a="10.45"
b=int(a)
print(b)

o/p:
error
e"C:\Users\HP\Desktop\pythonprogramdec\test13.py", line 2, in <module>
    b=int(a)
      ^^^^^^
ValueError: invalid literal for int() with base 10: '10.



a="10.45"
b=float(a)
print(b)
print(type(b))

o/p:
10.45
<class 'float'>

a=12.34
b=int(a)
print(a,b)

o/p:
12.34 12

int convert to string
______________________

a=10
b=str(a)
print(type(a),type(b))
print(a*3)
print(b*3)

o/p:
<class int> <class str>
30
101010



a="10"
b="20"
c=a+b
print(c)
o/p:
1020



a=int("10")
b=int("20")
c=a+b
print(c)

o/p:
30


a="10"
b="20"
c=int(a+b)
print(c+3)

o/p:
1023




a=30
b=40
s=a+b
print("sum=",s)


o/p:
sum=70

Here data is modify every time save and compile
solve this program take input from keyboad

input()
____________
it is a predefined function take input from keyboad in program runtime.
by default it takes string type.

#wap take string from keyboad and display it
print("enter a string ")
nm=input()
print("vaule=",nm)

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string
muna das
vaule= muna das

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string
kuna das
vaule= kuna das


input() : it take one argument that must be string type.

#wap take string from keyboad and display it
nm=input("enter a string ")
print("vaule=",nm)

o/p:

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string muna
vaule= muna
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string kuna
vaule= kuna



#wap take string from keyboad and display it
nm=input("enter a string\n")
print("vaule=",nm)



#wap take two integer from keyboad and add it
print("enter integer number ")
no1=input()
print("enter another integer number ")
no2=input()
s=no1+no2
print("sum=",s)

o/p:
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter integer number
10
enter another integer number
20
sum= 1020



#wap take two integer from keyboad and add it
print("enter integer number ")
no1=int(input())
print("enter another integer number ")
no2=int(input())
s=no1+no2
print("sum=",s)


"""
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter integer number
10
enter another integer number
20
sum= 30

"""


print("enter rectangle length and breadth")
L=int(input())
B=int(input())
print("length=",L)
print("breadth=",B)
ar=L*B
print("area=",ar)
pr=2*(L+B)
print("perimetr=",pr)


o/p:
enter rectangle length and breadth
7
8
length= 7
breadth= 8
area= 56
perimetr= 30





#wap take student name rollno mark keyboad  and dispaly it
print("enter name rollno and mark ")
nm=input()
r=int(input())
m=float(input())
print("name=",nm)
print("rollno=",r)
print("mark=",m)

"""
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter name rollno and mark
m das
1
90.50
name= m das
rollno= 1
mark= 90.5
"""



print(pow(2,3))  #8
import math
print(pow(2,3))
print(math.pi)
print(math.pow(2,3)) #8.0

#wap take square side formkeyboad dsipaly side area and perimeter
print("enter square side ")
s=int(input())
ar=s*s
pr=4*s
print("side=",s)
print("area=",ar)
print("perimter=",pr)

o/p:
enter square side
5
side=5
area=25
perimeter=20




wap take a student 4 mark from keyboad dispaly all mark
totalmark and avaerage mark
print("enter mark1")
m1=int(input())
print("enter mark2")
m2=int(input())
print("enter mark3")
m3=int(input())
print("enter mark4")
m4=int(input())
total=m1+m2+m3+m4
avg=total/4
print("mark1=",m1)
print("mark2=",m2)
print("mark3=",m3)
print("mark4=",m4)
print("total=",total)
print("avg mark=",avg)


o/p:
enter mark1
90
enter mark2
80
enter mark3
70
enter mark4
80
mark1=90
mark2=80
mark3=70
mark4=80
total mark=
avg=

wap take circle radius from keyboad display radius area and perimetr


convert to f  to c

conver c to f

wap find the simple interset

wap take emp sarly from keyboad  da=30% hra=20% then
display basic sal da hra and total sal