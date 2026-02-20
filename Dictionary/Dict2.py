#Nested dictionary

d={"Std1":{"Name":"Arun","Roll":1,"Mark":90.50}},{"Std2":{"Name":"Manmath","Roll":2,"Mark":91.5}}
print(d)

o/p:-
({'Std1': {'Name': 'Arun', 'Roll': 1, 'Mark': 90.5}}, {'Std2': {'Name': 'Manmath', 'Roll': 2, 'Mark': 91.5}})






d={101:{"Name":"Arun","Age":18,"Mark":90.50},102:{"Name":"Manmath","Age":20,"Mark":91.5}}
print(d)
print(d[102]["Name"])

o/p:-
{101:{"Name":"Arun","Age":18,"Mark":90.50},102:{"Name":"Manmath","Age":20,"Mark":91.5}}
manmath






NStudent={}
d={}
print("Enter name : ")
d["name"]=input()
print("Enter Age : ")
d["Age"]=int(input())
print("Enter Course : ")
d["Course"]=input()
Student[101]=d
d={}
print("Enter name : ")
d["name"]=input()
print("Enter Age : ")
d["Age"]=int(input())
print("Enter Course : ")
d["Course"]=input()
Student[102]=d
d={}
print("Enter name : ")
d["name"]=input()
print("Enter Age : ")
d["Age"]=int(input())
print("Enter Course : ")
d["Course"]=input()
Student[103]=d
print(Student)


        or 


Student={}
d={}
for i in range(3):
    print("Enter name : ")
    d["name"]=input()
    print("Enter Age : ")
    d["Age"]=int(input())
    print("Enter Course : ")
    d["Course"]=input()
    Student[i+1]=d
print(Student)






Student={}
d={}
n=int(input("Number of students : "))
for i in range(n):
    print("Enter Student",i+1," Data")
    print("Enter name : ")
    d["name"]=input()
    print("Enter Age : ")
    d["Age"]=int(input())
    print("Enter Course : ")
    d["Course"]=input()
    Student[i+1]=d
print(Student) 






students={}
n=int(input("How many students ? "))
for i in range(n):
    print("\nEnter details for student",i+1)
    roll=int(input("Roll No:"))
    name=input("Name:")
    age=int(input("Age:"))
    course=input("Course:")
    students[roll]={"name":name,"age":age,"Course":course}

print("\nAll student Data:")
print(students)

#Access Example
r=int(input("\nEnter roll number to check: "))
print("Name:",students[r]["name"])
print("Course:",students[r]["course"])
