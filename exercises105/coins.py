affirmative = ["Yes", "yes", "Y", "y", "yeah", "Yeah"]
coin = 0
answer = "yes"
while coin >= 0:
    print "You have %s coins." % coin
    answer = raw_input("Do you want another coin? ")
    if answer in affirmative:
        coin += 1
    else:
        print "Bye"
        break
