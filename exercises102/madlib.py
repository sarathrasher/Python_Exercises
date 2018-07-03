print "Please fill in the blanks below: \
____(name)____'s favorite food to eat is ____(food)___."

name = raw_input("What is name? ")
food = raw_input("What is food? ")
template = "%s's favorite food to eat is %s."
print template % (name, food)