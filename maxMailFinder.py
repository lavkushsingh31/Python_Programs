name = input("Enter file:")
handle = open(name)

histogram = dict()

for line in handle:
    if line.startswith('From') and len(line.split()) > 2:
        person = line.split()[1]
        histogram[person] = histogram.get(person, 0) + 1

maxSenderName = None
maxTimesSent = None

for key,value in histogram.items():
    if maxTimesSent is None or value > maxTimesSent:
        maxSenderName = key
        maxTimesSent = value

print(maxSenderName,maxTimesSent)
