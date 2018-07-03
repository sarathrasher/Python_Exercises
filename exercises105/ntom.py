i = 0
start_value = int(raw_input("Start from: "))
end_value  = 0

while end_value <= start_value:
    end_value = int(raw_input("End on: "))

for i in range (start_value, end_value + 1):
    print i
