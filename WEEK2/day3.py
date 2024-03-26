import re


# 305 555-1234
# (917) 555-5678
# (312) 555-7890
# (415) 555-2345
# (713) 555-6789
# (206) 555-8901
# (404) 555-3456
# (213) 555-6789
# (202) 555-9012
# (832) 555-4567

# ^ -> Start of the string
# [a-zA-Z0-9] -> checking for char/numbers inside the bracked
# + -> tracking occurences
# | -> or
# () -> grouping
# pattern = r'^[A-Za-z0-9]+@(gmail|yahoo|outlook)\.(net|com|org)'

# # print(re.search(pattern, email))
# # print(re.findall(pattern, email))
# email = "wal@gmail.com"

# name_pattern = r'^[a-z]{3}@gmail.com'

# if re.match(name_pattern, email):
#     print("Valid Email")
# elif re.match(name_pattern, email) == None:
#     print("Invalid Email")



# number = "305 555-1234"

# pattern = r'^\d{3} \d{3}-\d{4}$'

# if re.match(pattern, number):
#     print("Valid number")
# else: 
#     print("Invalid number")

#

sentence = "I have these following emails, walobwadan@gmail.com and ezekiel@gmail.com not forgetting zindua@zinduaschool.com"

pattern = r'\b[a-zA-Z]+@(?:gmail|zinduaschool)\.(?:com|net)'

print(re.findall(pattern, sentence))