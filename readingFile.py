print("Opening file 'readingFile.txt'")

try:
    filename = "readingFile.txt"
    handle = open(filename)
except:
    filename = input("Oops, file 'readingFile.txt' not found, enter the name of different file: ")
    handle = open(filename)

print("\nThe contents of the file '"+filename+"' are: \n")
for line in handle:
    print(line)
