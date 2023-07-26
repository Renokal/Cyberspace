import sys

dataFile = sys.argv[1]
checkSumSize = int(sys.argv[2])

with open(dataFile, 'rb') as f:
    data = f.read()

content = data.decode()

if checkSumSize not in [8, 16, 32]:
    print("Valid checksum sizes are 8, 16, or 32")
    exit(0)

print("")

if checkSumSize == 16:
    remainder = len(content) % 2
    if remainder != 0:
        padding_length = 2 - remainder
        content += 'X' * padding_length
elif checkSumSize == 32:
    remainder = len(content) % 4
    if remainder != 0:
        padding_length = 4 - remainder
        content += 'X' * padding_length

if checkSumSize == 8:
    checksum = sum(data) & 0xFF
elif checkSumSize == 16:
    
    checksum = 0
    for i in range(0, len(content), 2):
        word = (ord(content[i]) << 8) + ord(content[i + 1])
        checksum = (checksum + word) & 0xFFFF
elif checkSumSize == 32:
    
    checksum = 0
    for i in range(0, len(content), 4):
        word = (ord(content[i]) << 24) + (ord(content[i + 1]) << 16) + (ord(content[i + 2]) << 8) + ord(content[i + 3])
        checksum = (checksum + word) & 0xFFFFFFFF

print(content)
print(checkSumSize,"bit","checksum","is "f"{checksum:0{checkSumSize // 4}x}","for all  ",len(content), "chars")
