import time
countdown = 0
while countdown <= 0:
    count = int(raw_input("How long until liftoff?\n"))
    if count >= 20:
        print "Please enter a number less than 20."
    elif count <= 0:
        print "Please enter a number greater than zero."
    elif: count != 
    else: 
        countdown += count

i = 0
for i in range (countdown, -1, -1):
    time.sleep(1)
    print i
    if i <= 0:
        time.sleep(1)
        print "We have liftoff!"