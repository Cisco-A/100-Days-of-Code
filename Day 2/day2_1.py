#A program to calculate tip given at a resturant
#note: all instances of 'dp' mean 'Decimal Places'

#Initialization



print('Welcome to the tip calculator')

#Calculations

initial_bill = float(input('What was the total bill? $'))

tip = int(input('What percentage tip would you like to give? '))
tip_percentage = tip/100

final_bill = (tip_percentage * initial_bill) + initial_bill

split_number = int(input('How many people to split the bill? '))

# result = round(final_bill / split_number, 2) #This does not return 2 dp when its original caluclation ends with one dp

result = "{:.2f}".format(final_bill / split_number, 2) #More accurate to return all values in 2dp

#Output

print(f'Each person should pay: ${result} ')