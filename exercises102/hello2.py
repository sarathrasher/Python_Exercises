name = raw_input("What is your name? ".upper())
upper_name = name.upper() 
#.upper() is called a "method" and is only used for a string, gets first precedence
length = len(name)
print "hello, ".upper() + upper_name + "!"
string = ("your name has %s letters in it! awesome!" % length).upper()
print string