count = 1
total = 0

#BUG: the line below required closing full colon (:) the count<5 needs <= to include the numeber 5#
while count <= 5:
    total = total + count
    count = count + 1
#BUG: print statement had total at the end. The program cannot concatenate integers so we put the integer inside quotation marks ("")#
print(f"Sum of 1 to 5 is: {total}")