file = open("copy_target.txt", "w")
text1 = ["Hello\n", "My name is JOHN\n", "Bye"]
for i in text1:
    file.write(i)
file.close()
num_lines = 0
with open("copy_target.txt", "r") as file1, open("copy_target2.txt", "w") as file2:
    for line in file1:
        file2.write(line.lower())

with open("copy_target2.txt", "r") as file2:
    for line in file2:
        print(line)
        num_lines += 1
print("Total number of lines copied: ", num_lines)
