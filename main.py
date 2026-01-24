#TASK N1
def toKm(a) -> float:
 return round((a * 1.61), 2)
def toMiles(a) -> float:
 return round((a / 1.61), 2)
while True:
    try:
        option = int(input("Choose between 0 and 1+\n0: convert to Miles\n1+: convert toKilometers: "))
    except:
        print("Error happened\ntry again")
        continue
    if option > 0:
        a = float(input("Write n km's to convert to miles: "))
        print(f"{a} kilometers is {toMiles(a)} miles")
    else:
        a = float(input("Write n miles to convert to km's: "))
        print(f"{a} miles is {toKm(a)} kilometers")
usd = 519.74
euro = 609.91
difference = usd / euro
print(difference)
def toEUR(a) -> float:
 return round((a * difference), 2)
def toUSD(a) -> float:
 return round((a / difference), 2)
while True:
    try:
        option = int(input("Choose between n>0 and n<0 for\nn<=0: convert to USD\nn>0:convert to EURO:\n"))
    except:
        print("Error happened\ntry again")
        continue
    if option > 0:
        a : int = int(input("Write n amount of USD: "))
        print(f"{a} USD is {toEUR(a)} EURO")
    else:
        a : int = int(input("Write n amount of EURO: "))
        print(f"{a} EURO is {toUSD(a)} USD")
#TASK N2
a : int = int(input("Write a: "))
b : int = int(input("Write b: "))
print(f"Hypotenuse length is {(a**2 + b**2) ** 0.5}")
def eventEnd(a : int, b : int, c : int) -> str:
 extra_hour = (b + c) // 60
 hour = a + extra_hour
 mins = (b + c) % 60
 if hour >= 24:
    hour %= 24
 print(hour, mins, sep=":")
a : int = int(input("Write starting time (hours): "))
b : int = int(input("Write starting time (minutes): "))
c : int = int(input("Write event duration (minutes): "))
if a < 0 or b < 0 or c < 0:
 print("parameters should be more then 0")
else:
 eventEnd(a, b, c)