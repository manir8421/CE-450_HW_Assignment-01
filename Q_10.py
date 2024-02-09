
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 10

def amc(n):                              # define function where parameter in n

    def sum_div(m):                      # define function for divisible check where parameter in m

        div_sum = 0                      # take variable for store exact divisable value
        for j in range(1, m):            # loop for check for divisor
            if m % j == 0:
                div_sum += j
        return div_sum                   # return the calculated sum

    amic_num = n + 1                     # check the smallest amicable greater then input value

    while True:                          # find the smallest amicable value
        sum_amic = sum_div(amic_num)
        if sum_div(sum_amic) == amic_num and sum_amic != amic_num:    # check the value is proper divisor or not
            return amic_num              # return the smallest amicable value
        amic_num += 1

# Input  from keyboard by the user and check it's positive interger or not
try:
    num = int(input("Enter the value as an integer that is positive number: "))
    if num <= 0:
        raise ValueError("\nInvalid input! Please enter a positive integer.")
except ValueError as ve:
    print(ve)
    exit()

# Print the output result
print(f"\nSmallest amicable number of {num} and greater than ({num}) is: {amc(num)}")
