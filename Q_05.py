
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 05


def lrgst_factor(m):                                    # define a function and parameter in m
    factors = []                                        # empty list to store factors
    for input_num in range(1, m):                       # range from 1 to m - 1
        if m % input_num == 0:                          # Check if input number is a factor of m
            factors.append(input_num)                   # it the input number is a factor, store to the list
    return factors, max(factors) if factors else None   # Return the list of factors and the maximum value

# Input from keyboard by the user
try:
    m = int(input("Type a number from keyboard for to find factors\t\t: "))
except ValueError:
    print("Please type a valid integer.")
    exit()

# Call the function with user input
factors, max_factor = lrgst_factor(m)

# Print the factors list and maximum value
if factors:
    print("\nFactors list of", m, "are\t\t\t\t\t:", factors)
    print("The largest integer value and evenly divides", m,"is\t:", max_factor)
else:
    print("\nThere are no any factors for the input number.")


