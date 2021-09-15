def temperature_recursion():
    temp = int(input("Enter temperature : "))
    if temp == 100:
        print("good-bye!!")
        return temp
    if temp > 100:
        print("hot")
    if temp < 60:
        print("cold")
    if 61 <= temp <= 99:
        print("just right")
    temperature_recursion()
# temperature_recursion() 

def temperature_while_loop():
    temp = int(input("Enter temperature : "))
    while temp != 100:
        if temp >= 100:
            print("hot")
        elif temp <= 60:
            print("cold")
        if temp >= 61 and temp <= 99:
            print("just right")
        temp = int(input("Enter temperature : "))
    print("good-bye!!")
    return temp
# temperature_while_loop()

import sys
def temperature_for_loop():
    
    for _ in range(sys.maxsize**10):
        temp = int(input("Enter temperature : "))
        if temp >= 100:
            print("hot")
        elif -99 <= temp <= 60:
            print("cold")
        elif temp >= 61 and temp <= 99:
            print("just right")
        elif temp == 100:
            print("good-bye!!")
            return temp 
# print(temperature_for_loop())
