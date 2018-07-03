
def bill_amount():
    bill_input = 0
    while bill_input <= 0:
        bill_input = int(raw_input("How much was the bill?\n"))
        if bill_input > 0: 
            bill = float(bill_input)
            return bill
        else:
            print "Please enter a positive number."
  
bill_amount()

def service_level():
    service = ["good", "bad", "fair"]
    service_rating = ""
    while service_rating != 'good' or 'fair' or 'bad':
        service_rating = raw_input("How was your service?\n")
        rating = service_rating.lower()
        if rating in service:
            return rating
        else:
            print "Please enter either 'good', 'fair', or 'bad'."
            
service_level()

def tip_calc():
    if rating == "good": 
        tip = bill * 0.20
    elif rating== "fair": 
        tip = bill * 0.15
    else: 
        tip = bill * 0.10  
    total = bill + tip
    print  "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total
    return tip
    return total

tip_calc()
