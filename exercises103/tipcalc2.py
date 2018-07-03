bill_input = raw_input("How much was the bill? \n")
bill = float(bill_input)

service_rating = raw_input("How was your service? \n")
rating = service_rating.lower()
split = raw_input("Split how many ways?")

def tip_calc():
    if rating == "good": 
        tip = bill * 0.20
    elif rating== "fair": 
        tip = bill * 0.15
    elif rating == "bad": 
        tip = bill * 0.10  
    else: 
        print "Please input either 'good' or 'fair' or 'bad'."
        return
    total = bill + tip
    adjust_total = total / split
    print  "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total
    print "Total amount per person: %.2f" % adjust_total
    return tip
    return total
    return adjust_total
    
tip_calc()