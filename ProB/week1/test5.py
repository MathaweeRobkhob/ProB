
print("* Convert BMI *")

weight = float(input("Enter your weight (kg): "))

height_m = float(input("Enter your height (m): "))

bmi = weight / (height_m ** 2)

print(f"Your BMI is: {bmi:.5f}")