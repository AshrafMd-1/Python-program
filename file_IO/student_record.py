file = open("student_record.txt", "w")
n = int(input("Enter the number of students records you want to store: "))
for i in range(n):
    name = input("Enter the student name: ")
    rollnumber = input("Enter the roll number: ")
    branch = input("Enter the branch: ")
    file.write(name + " " + rollnumber + " " + branch + "\n")
file.close()
file = open("student_record.txt", "r")
branch = input("Enter the branch to display students record: ")
str = file.readlines()
for line in str:
    lst = line.split()
    if branch == lst[-1]:
        print(line)
file.close()
