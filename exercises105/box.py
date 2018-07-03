
width = raw_input("Width? " )
height = raw_input("Height? " )
cols = int(width)
row = int(height)
#print "*" * width
#for i in range(0, height - 2):
#    print "*" + " " * (width - 2) + "*"
#print "*" * width


for i in range(0, row, 1):
    star = ""
    for j in range(0, cols, 1):
        if i == 0 or i == row - 1:
            star += "*"
        elif j == 0 or j == cols - 1: 
            star += "*"
        else:
            star += " "
    print star



