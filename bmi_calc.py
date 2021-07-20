print("This program claculates yout body mass index")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = float(weight / (height ** 2))

print("Your BMI is: ", bmi)

if (bmi > 18.5 and bmi <= 24.9):
    print("The classification of your BMI is Normal weight")
elif (bmi >= 25 and bmi <= 29.9):
    print("The classification of your BMI is Overweight")
elif (bmi >= 30):
    print("The classification of your BMI is Obesity")
else:
    print("The classification of your BMI is Underweight")