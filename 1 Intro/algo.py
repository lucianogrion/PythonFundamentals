import re
stringa = str(input())

#your code goes here
pattern = r"[1,8,9]{1,1}[0-9]{7,7}"

if re.match(pattern, stringa):
    print("Valid")
else:
    print("Invalid")
