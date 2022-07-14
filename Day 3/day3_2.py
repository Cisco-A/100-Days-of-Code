#BMI calculator V2.0

#Inputs
height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = round(weight / (height ** 2))

#Conditions

# if bmi < 18.5:
#     print("You are underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print("You have a normal weight")
# elif bmi >= 25 and bmi < 30:
#     print("You are overweight")
# elif bmi >= 30 and bmi < 35:
#     print("You are obese")
# else:
#     print("You are clinically obese.")    

    #The above code is too bogus with unecessary statements
    #Note: Take a look at lines 11 and 13... 
    #The program already knows <18.5 therefore there is no need for ">=18.5" 
    #as it is already implied by line 13... The same applies to the other statements

#Below is an optimized and better version of the program

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underwe1ight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")