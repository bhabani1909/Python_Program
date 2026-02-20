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