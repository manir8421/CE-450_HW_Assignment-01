
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 07


def same_ord(a, b):   # Define function where the parameters are a,b

    return len(str(a)) == len(str(b))  # check the length of input and return answer to function

# Input from keyboard by the user and check that input is valid / invalid
try:
    a = int(input("Enter the first positive integer\t: "))
    if a <= 0:
        raise ValueError("\nInvalid input! Please enter a positive integer.")
    
    b = int(input("Enter the second positive integer\t: "))
    if b <= 0:
        raise ValueError("\nInvalid input! Please enter a positive integer.")
    
except ValueError as error:
    print(error)
    exit()

# Print the output result
print(f"\nAre the bit counts of {a} and {b} the same? {same_ord(a, b)}")





