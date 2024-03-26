#CONDITIONAL EXECUTIONS & OPERATORS AND FUNCTIONS
name = "John"
school = "Zindua School"

if name != "Dan" and school == "Zindua":
    print("Hello Dan")
elif name == "James":
    print("Hello James")
else:
    print("Hello Stranger")

# match name:
#     case "Dan":
#         print("Hello Dan")
#     case "John":
#         print("Hello John")
#     case _:
#         print("Hello Stranger")

#Operators
#Arithmetic Operators
# + 
# -
# *
# /
# %
# **
# //
        
#Logical Operators && and ||
# and
# or
    
#Comparison Operators
# ==
# !=
# !
# >
# <
# >=
# <=


#Function declaration
def add_number(num1, num2): #Parameters -> functions expect
    print(num1 + num2) #Function definition

#function call
add_number(2, 3) #Arguments -> actual values