from email.errors import BoundaryError
from webbrowser import Error


def get_int_input(message):
    while True:
        try:
            temp = int(input(message))
            if (temp > 1) and (temp < 37):
                return temp
            else:
                print("Number must be between 2 and 36")
        except ValueError:
            print("Make sure you give a whole number.")


#get all clean user inputs
num_orders = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
              "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
base_input = get_int_input("What base input?     ")
looping = True
while looping:
    looping = False
    input_num = input("Input number:    ")
    for item in input_num:
        if item in num_orders[:base_input:]:
            pass
        else:
            looping = True
            print("Input outside of range.")
            break
base_output = get_int_input("What base output?     ")

#convert input to num
reverced_input = input_num[::-1]
sum_total = 0
for index, item in enumerate(reverced_input):
    char_value = num_orders.index(item)
    sum_total += char_value*(base_input**(index))

#convert num to desired output
counter = 1
while base_output**counter <= sum_total:
    counter += 1
length_of_output = counter
output_string = ""
reverce_index = length_of_output
for index in range(1, length_of_output+1):
    temp_num = sum_total // (base_output**(reverce_index-1))
    sum_total -= temp_num*(base_output**(reverce_index-1))
    output_string = output_string + num_orders[temp_num]
    reverce_index -= 1
print(output_string)
