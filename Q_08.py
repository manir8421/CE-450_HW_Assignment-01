
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 08


def double_5(n):                              # define function where parameter is n
    con_num = str(n)                          # Convert the number to a string

    # loop start
    for i in range(len(con_num) - 1):     
        if con_num[i] == '5' and con_num[i + 1] == '5':        # condition check and return the result True
            return True   
    return False                              # if not match the condition then return the result False

try:
    num = int(input("Enter (type from keyboard) an integer number\t\t: "))      # Input from kayboard by the user
except ValueError:
    print("\nInvalid input! Please enter a valid integer.")    # error is input is not integer
    exit()

# Print the output result
print(f"\nCheck {num} for 'contain two adjacent 5s', The resulr is\t: {double_5(num)}")



