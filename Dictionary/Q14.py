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