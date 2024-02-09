
# Md_Maniruzzaman_ID:20099
# CE 450 / HW assignment - 01
# Question : 01


def if_function(condition, true_result, false_result):  # if_function function declare where parameters are condition, true_result, false_result
    try:                                                # try to execute the block, if there any exception occur, then execute except
        condition_value = bool(eval(condition))         # convert a string to integer and do a boolean function
        if condition_value:                             # condition check
            return eval(true_result)
        else:
            return eval(false_result)
    except:
        return false_result

condition = input("Enter the situation you wish\t\t: ")   # condition input
true_result = input("Type the first value here\t\t: ")    # value input
false_result = input("Type the second value here\t\t: ")  # value input

result = if_function(condition, true_result, false_result)  # function call and collect result

print(f"\nResult for the ({condition}) condition is\t:", result)
