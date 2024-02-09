
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 02



def sum_odd_number(vlu):  # define function where parameter in vlu

    sum_result = 0                # take variable for store result
    for m in range(1, vlu + 1):   # loop for calculation
        if m % 2 != 0:
            sum_result += m
    return sum_result             # return result to function

try:      # taking input and try-except block run for print output and check input is integer or not
    vlu = int(input("Enter an integer number: "))  # Take input from the user
    print(f"\nOutput result for the value ({vlu}) is: {sum_odd_number(vlu)}") 
except ValueError:
    print("Invalid input! Please enter a valid integer.")
