height = int(raw_input("How tall is this pyramid? "))

wide = height * 2 - 1
for i in range(1, (stars + 2), 2):
    total_spaces = stars - i
    side_spaces = total_spaces / 2
    print " " * side_spaces + "*" * i + " " * side_spaces
