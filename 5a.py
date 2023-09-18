import re

def isphonenumber(numStr):
    return len(numStr) == 12 and numStr[3] == numStr[7] == '-' and numStr[:3].isdigit() and numStr[4:7].isdigit() and numStr[8:].isdigit()

def chkphonenumber(numStr):
    return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', numStr))

ph_num = input("Enter a phone number: ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using Regular Expression")
if chkphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
