#program no 1
# program that calculates age
print("Age Calculator")
def ageCalculator()-> int:
    current_year:int= int(input("Enter the current year:"))
    birth_year:int = int(input("Enter your birth year: "))
    age:int=current_year-birth_year
    return age
output = ageCalculator()
print("Your age is:", output ,"years")

#/*************************************************************
#program no 2
# program that calculates the area of rectangle
print("rectangular area calculator")
def calculateArea() -> float:
    length:float = float(input("Enter the length: "))
    width:float = float(input("Enter the width: "))
    area:float = length * width
    return area
outputofarea = calculateArea()
print("The area of the rectangle is:", outputofarea ,"metersquared")

# /****************************************************************
#program no 3
# program that calculates the area of circle
print("circle Area Calculator")
def calculateAreaofCircle() -> float:
    radius:float = float(input("Enter the radius of the circle : "))
    area:float = 3.14 * radius * radius
    return area
outputofarea = calculateAreaofCircle()
print("The area of the Circle is : " , outputofarea ,"metersquared")

# /****************************************************************
#program no 4
# program that calculates the area of cube

print("cube area calculator")
def calculateAreaofCube() -> float:
    side:float = float(input("Enter the side of the cube: "))
    area:float = side * side * side
    return area
outputOfCube = calculateAreaofCube()
print("The area of the Cube is : " , outputOfCube , "metercube")

# /****************************************************************
#program no 5
# program that calculates the volume of cylinder
print("volumeOfCylinderCalculator")
def calculateVolumeOfCylinder() -> float:
    radius:float = float(input("Enter the radius of the cylinder: "))
    height:float = float(input("Enter the height of the cylinder: "))
    volume:float = 3.14 * radius * radius * height
    return volume
outputOfCylinder = calculateVolumeOfCylinder()
print("The volume of the Cylinder is : " , outputOfCylinder , "metercube") 

# /****************************************************************
#program no 6
#  program that calculates the percentage
print("PercentageCalculator")
def calculatePercentage() -> float:
    totalNumber:float = float(input("Enter the  total numbers: "))
    obtainedNumber:float = float(input("Enter the  obtained numbers: "))
    percentage:float = (obtainedNumber / totalNumber) * 100
    return percentage
outputOfPercentage = calculatePercentage()
print("The percentage is : " , outputOfPercentage ,"%")

#  /****************************************************************
#program no 7
# program that converts temperature from celcius to fahrenheit
print("temperature convertor program")
def convertTemperature() -> float:
    temperature:float = float(input("Enter the temperature in Celsius: "))
    result:float = (temperature * 9/5) + 32
    return result
outputOfTemperature = convertTemperature()
print("The temperature in Fahrenheit is: ", outputOfTemperature , " degrees")

# /****************************************************************
#program no 8
# program that converts temperature from fahrenheit to Celsius
print("temperature convertor program")
def convertTemperatureToCelsius() -> float:
    temperature:float = float(input("Enter the temperature in Fahrenheit: "))
    result:float = (temperature - 32) * 5/9
    return result
outputOfTemperatureToCelsius = convertTemperatureToCelsius()
print ("the temperatue in celsius is : ",outputOfTemperatureToCelsius ," degrees")

# /****************************************************************
#program no 9
# program that converts minutes into seconds
print("time convertor program")
def convertMinutesToSeconds() -> float:
    minutes:float = float(input("Enter the minutes: "))
    seconds:float = minutes * 60
    return seconds
outputOfMinutesToSeconds = convertMinutesToSeconds()
print("The time in seconds is: ", outputOfMinutesToSeconds , " seconds")

# /****************************************************************
#program no 10
# program that calculates BMI
print("BMI calculator program")
def calculateBmi() -> float:
    weight:float = float(input("Enter your weight in kilograms: "))
    height:float = float(input("Enter your height in meters: "))
    bmi:float = weight / (height * height)
    return bmi
outputOfBmi = calculateBmi()
print("Your BMI is: ", outputOfBmi)

# /****************************************************************