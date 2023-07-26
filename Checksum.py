"""
/*=============================================================================
| Assignment: pa02 - Calculating an 8, 16, or 32 bit
| checksum on an ASCII input file
|
| Author: Andrew Taylor
| Language: c, c++, Java, GO, Python
|
| To Compile: javac pa02.java
| gcc -o pa02 pa02.c
| g++ -o pa02 pa02.cpp
| go build pa02.go
| python pa02.py //Caution - expecting input parameters
|
| To Execute: java -> java pa02 inputFile.txt 8
| or c++ -> ./pa02 inputFile.txt 8
| or c -> ./pa02 inputFile.txt 8
| or go -> ./pa02 inputFile.txt 8
| or python-> python3 pa02.py inputFile.txt 8
| where inputFile.txt is an ASCII input file
| and the number 8 could also be 16 or 32
| which are the valid checksum sizes, all
| other values are rejected with an error message
| and program termination
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Summer 2023
| Instructor: McAlpin
| Due Date: per assignment
|
+=============================================================================*/
"""

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

"""
/*=============================================================================
| I [Andrew Taylor] ([an282352]) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================*/
"""