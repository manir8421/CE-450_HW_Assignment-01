
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 06


def pfct_num(n):
    # calculation for perfect number
    sum_fact_num = sum([m for m in range(1, n) if n % m == 0])
    return sum_fact_num == n

# Input from the user and start try-except block
try:
    n = int(input("Type the input integer number\t\t\t: "))
except ValueError:
    print("\nPlease enter a valid integer.")
    exit()

# Print whether the input number is a perfect number or not
print("\nIs the input number", n, "a perfect number? Answer\t:", pfct_num(n))


