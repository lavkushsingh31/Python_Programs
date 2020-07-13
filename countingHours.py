
print("Opening file 'maildata.txt'")

try:
    filename = "maildata.txt"
    handle = open(filename)
except:
    filename = input("Oops, file 'maildata.txt' not found, enter the name of different file: ")
    handle = open(filename)

histogram = dict()

for line in handle:
    if line.startswith('From') and len(line.split()) > 2:
        splittedLine = line.split()
        hour = splittedLine[5].split(':')[0]
        histogram[hour] = histogram.get(hour, 0) + 1

for key, value in sorted(histogram.items()):
    print(key,value)
