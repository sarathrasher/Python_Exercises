first_name = raw_input("Please enter a first name. ")
last_name = raw_input("Please input a last name. ")

#Concatenation example
message = "Hi, " + first_name + " " + last_name + " I saw your resume on LinkedIn and would like to hire you."
length = len(message)
#"print" is  a unary operator. You don't use parentheses
# Parentheses: change order of operations, invoke a function, create a tuple
print length 
print message

message = "Hi, %s %s I saw your resume on LinkedIn and would like to hire you." % (first_name, last_name) 
# Group of arguments is called a "tuple." Tuples cannot be changed ("immutable").
length = len(message)
print length
print message