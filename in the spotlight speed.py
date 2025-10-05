#"in the spotlight" page 184 :
#Designing a count controlled loopo with the for statement"
#MPH = KPH * 0.6214 convert from kilometers to miles per hour
#range(60, 131, 10)

#This program converts the speeds 60 kph through 130 kph
#in increments of 10 kph to  mph

STARTING_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONV_FACTOR = 0.6214

#PRINT THE TABLE HEADINGS
print()
print("KPH/tMPH")
print("-------------------")

#PRINT THESE SPEEDS:
for kph in range(STARTING_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONV_FACTOR
    print(f"{kph}\t{mph:.1f}")
