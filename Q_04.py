
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 04


def df(x, y, z):

    try:    # starts the try-except block, if there any exception occur, then execute except
        x = int(input("Type the first value for 'x'\t: "))
        y = int(input("Type the second value for 'y'\t: "))
        z = int(input("Type the third value for 'z'\t: "))
    except ValueError:
        print("Please enter a valid integer.")
        return False

    # Calculation of subtraction and result check with another value
    calc_input = any([z - x == y, z - y == x, y - x == z, y - z == x, x - y == z, x - z == y])
    return calc_input


# Call the function with user input
result = df(0, 0, 0)

# Print the output (True/False) according to input value and calculation
print("\nThe Output result is\t\t:", result)
