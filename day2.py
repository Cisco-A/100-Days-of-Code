#Calculating Life Expectancy

# Initial version by me... Its too bogus

# age_now = int(input('Enter your cuurent age: \n'))

# years_till_90 = 90 - age_now
# months_till_90 = (12*90) - (age_now * 12)
# weeks_till_90 = (52 * 90) - (age_now * 52)
# days_till_90 = (365 * 90) - (age_now * 365)

# print(f"You have {years_till_90} years, {months_till_90} months {weeks_till_90} weeks and {days_till_90} days to live.")


#Optimized version

age_now = int(input('Enter your cuurent age: \n'))

years_till_90 = 90 - age_now
months_till_90 = years_till_90 * 12
weeks_till_90 = years_till_90 * 52
days_till_90 = years_till_90 * 365

print(f'You have {years_till_90} years, {months_till_90} months, {weeks_till_90} weeks and {days_till_90} days to live.')