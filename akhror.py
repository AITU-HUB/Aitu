#TASK 1

income=float(input("Enter income: "))
if income<=85528:
    tax=income*0.18-556.02
else :
    tax=14839.02+(income-85528)*0.32
if tax<0:
    tax=0
print(round(tax))

#TASK 2 
 
year = int(input("Enter year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")


#TASK 3 

blocks = int(input("Enter number of blocks: "))

height = 0
needed = 1

while blocks >= needed:
    blocks -= needed
    height += 1
    needed += 1

print(height)
