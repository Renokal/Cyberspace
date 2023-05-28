# user requirements:Minimum 8 characters:
# The alphabet must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ].

import re

redMark = 0
password = input("Password: ")

while True:
 if (len(password) <= 8):
         redMark = -1
         break
 elif not re.search("[a-z]",password):
         redMark = -1
         break
 elif not re.search("[A-Z]",password):
         redMark = -1
         break
 elif not re.search("[0-9]",password):
         redMark = -1
         break
 elif not re.search("[_@$]",password):
         redMark = -1
         break
 elif re.search("\s",password):
        redMark = -1
        break
 else:
       redMark == 0
       print("Strong Password")
       break
      
if redMark == -1:
   print("Weak Password")      