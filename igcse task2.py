# GCSE TASK (BABY TEMPERATURE)
from array import *
print("BABY TEMPERATURE CHECKER")
MinBbyTemp = 36.0
MaxBbyTemp = 37.5  # in degree Celsius
routTemp = array("i", [])  # array to store routine checks
NoBabyTemp = int(input("How many temperatures are you inputting? "))
for temp in range(NoBabyTemp):
    BabyTemp = int(float(input("What is the temperature of the baby? ")))
    array = [BabyTemp]
    if MaxBbyTemp < BabyTemp:
        print("The temperature of the baby is too high and above the average.")
    elif BabyTemp < MinBbyTemp:
        print("The temperature of the baby is low/unusual and needs to be worked on.")
    elif (BabyTemp > MinBbyTemp) and (BabyTemp < MaxBbyTemp):
        print("The temperature is within a healthy range.")
    else:
        print("The temperature is not acceptable")
    routTemp.append(BabyTemp)
for temp in range(NoBabyTemp):
    print(routTemp[temp], end=" ")
highest = max(routTemp)
lowest = min(routTemp)
difference = highest - lowest
print("The highest temperature is ", highest)
print("The lowest temperature is ", lowest)
print("The difference between", highest, "and", lowest, "=", difference)
# end of code
