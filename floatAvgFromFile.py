# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
floatSum = 0;
floatsFound = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    floatsFound = floatsFound + 1
    colonIndex = line.find(":")
    value = float(line[colonIndex+1:].strip())
    floatSum = floatSum + value
average = floatSum/floatsFound
print("Average spam confidence:", average)
