#Rollercoaster ticketing

height = int(input("Enter your height: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoasrter")
    age = int(input("How old are you? "))
    if age < 12:
        bill += 5
        print(f"Your ticket price is ${bill}")
    elif age <= 18:
        bill += 7
        print(f"Your ticket price is ${bill}")
    elif age >= 45 and age <= 55: #Midlife crisis age range
        print("Everything is going to be ok. Have a free ride on us.")
    else:
        bill += 12
        print(f"Your ticket price is {bill}")

    want_photo = input("Do you want a photo? 'Y' or 'N': ")
    if want_photo == "Y":
        bill += 3
    print(f"Your total bill is {bill}")
   

else:
    print("You cannot ride the rollercoaster.")