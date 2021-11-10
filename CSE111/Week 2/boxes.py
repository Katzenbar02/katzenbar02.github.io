import math

numI = int(input("Enter the number of items: "))
numPB = int(input ("Enter the number of items per box: "))

numBox = str(math.ceil(numI / numPB))
connumI = str(numI)
connumPB = str(numPB)


print("For " + connumI + " items, packing " + connumPB + " items in each box, you will need " + numBox + " boxes.")