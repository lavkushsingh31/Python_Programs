#This program will take a file as input and will generate a list containing each word of the file, removing duplicates and in sorted fashion

listOfWords = list()

print("Opening file 'PlayingwithStrings.txt'")

try:
    filename = "PlayingwithStrings.txt"
    handle = open(filename)
except:
    filename = input("\nOops, file 'PlayingwithStrings.txt' not found, enter the name of different file: ")
    handle = open(filename)

for line in handle:
    for word in line.split():
        if word not in listOfWords:
            listOfWords.append(word)

print(sorted(listOfWords))
