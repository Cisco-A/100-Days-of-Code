# Paint Calculator
import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)# math.ceil is to round up the number
    print(f"you'll need {number_of_cans} of paint")
  

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


