def calculate_grade(average):
    if average>=90:
        return 'A+'
    elif average>=80:
        return 'A'
    elif average>=70:
        return 'B'
    elif average>=60:
        return 'C'
    elif average>=50:
        return 'D'
    else:
        return 'F'

Name=input("Enter student name:")
Rollno=input("Enter your rollno:")

marks=[]
for i in range(1,4):
    mark=int(input(f"Enter your marks for subject{i}:"))
    marks.append(mark)

total = sum(marks)
average = total/len(marks)
grade = calculate_grade(average)

print("\n----Report card------")
print(f"Name:{Name}")
print(f"Rollno: {Rollno}")
print(f"Totalmarks: {total}")
print(f"average: {average:.2f}")
print(f"Grade: {grade}")
