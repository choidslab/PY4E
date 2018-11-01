filename = input("Enter a filename:")
fhand = open(filename, 'rt')

count = 0
words = list()

for line in fhand:
    if line.startswith("From: "):
        count += 1
        words.append(line.split()[1])

for word in words:
    print(word)
print("There were", 27, "lines in the file with From as the first word")