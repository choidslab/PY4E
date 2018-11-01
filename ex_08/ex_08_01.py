filename = input("Enter file:")
fhandle = open(filename, 'rt')
str_file = fhandle.read()
result = str_file.split()
print(sorted(result))

