fname = input("Enter file name: ")
f = open(fname, "r")
data = f.read()
num_chars = len(data)
f.close()
num_words = 0
num_lines = 0
with open(fname, "r") as f:
    for line in f:
        num_lines += 1
        words = line.split()
        num_words += len(words)
print("Number of words: ", num_words)
print("Number of lines: ", num_lines)
print("Number of characters: ", num_chars)
