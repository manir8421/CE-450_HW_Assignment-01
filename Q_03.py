
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 03


def foo(a, b, c, d):   # define function "foo" where parameters are a,b,c,d

    input_num_list = [a, b, c, d]  # declare a variable for make a list of input value
    
    sorted_input_number = sorted(input_num_list) # shorted the input number list to find the smallest two numbers
    
    # make square of first 2 number
    square = []
    for a in sorted_input_number[:2]:
        square.append(a ** 2)
    
    # summatation of square and return to function
    sum_square = 0
    for num in square:
        sum_square += num

    return sum_square
# Input from the keyboard by the user
a = int(input("Type the input value for 'a'\t\t: "))
b = int(input("Type the input value for 'b'\t\t: "))
c = int(input("Type the input value for 'c'\t\t: "))
d = int(input("Type the input value for 'd'\t\t: "))

# Call the function "foo" for the output result
result = foo(a, b, c, d)
print("\nSum for the 2 smallest values square is\t:", result)

