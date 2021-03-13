
a = float(input()) / 100
b = float(input())

BMI = b / (a * a)

if BMI < 18.5:
    result = "Underweight"

elif 18.5 < BMI < 24.9:
    result = "Normal"

elif 24.9 < BMI < 29.9:
    result = "Overweigth"

elif 29.9 < BMI < 34.9:
    result = "Obese"

elif 34.9 < BMI:
    result = "Extremely Obese(Kamtar Bokhor:|)"

else:
    result = "Error!!!"


print("BMI =",result)