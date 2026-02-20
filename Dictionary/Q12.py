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