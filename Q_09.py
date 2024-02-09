
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 09


def uniq_digits(x):
    
    num_string = str(x)                                                    # Convert the input integer to string
    unique_digits = sorted(set(num_string))                                # set to store unique digits and sorted
    
    print(f"\nUnique digits in ({x}) are: {' '.join(unique_digits)}")      # Print the unique digits
    
    return len(unique_digits)                                              # return unique digits to function

try:
    num = int(input("Enter a positive integer\t: "))                       # Input from the user
    if num <= 0:                                                           # check the input is positive integer or not
        raise ValueError("\nInvalid input! Please enter a positive integer.")  # error message
except ValueError as error:
    print(error)
    exit()

# print the output result
print(f"The number of unique digits in ({num}) is: {uniq_digits(num)}")

