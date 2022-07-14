#A Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Lets see 
#Tip: Use the count() and lower() function where necessary

#Note: instead of this bogus, you can concatenate the 2 inputs and find
#Their true and love count together
lower_name1 = name1.lower()
lower_name2 = name2.lower()

#Counting for "TRUE"
#First name
t1 = lower_name1.count("t")
r1 = lower_name1.count("r")
u1 = lower_name1.count("u")
e1 = lower_name1.count("e")

l1 = lower_name1.count("l")
o1 = lower_name1.count("o")
v1 = lower_name1.count("v")
e1_2 = lower_name1.count("e")

total1 = t1 + r1 + u1 + e1
total1_2 = l1 + o1 + v1 + e1_2
#Second name
t2 = lower_name2.count("t")
r2 = lower_name2.count("r")
u2 = lower_name2.count("u")
e2 = lower_name2.count("e")

l2 = lower_name2.count("l")
o2 = lower_name2.count("o")
v2 = lower_name2.count("v")
e2_1 = lower_name2.count("e")

total2 = t2 + r2 + u2 + e2
total2_1 = l2 + o2 + v2 + e2_1

#Adding each word total
true = total1 + total2
love = total1_2 + total2_1

true_love = str(true) + str(love)#Instead of the next step, you can do this: int(str(true) + str(love))

#convert true_love back to integer for use in control flow
fate = int(true_love)

#Control flow
if fate < 10 or fate > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif fate >= 40 and fate <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")