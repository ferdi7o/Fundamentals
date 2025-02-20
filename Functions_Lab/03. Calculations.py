def calculatioans(operator, num_one , num_two):
    results = 0
    if operator == "multiply":
        results = num_one * num_two
    elif operator == "divide":
        results = num_one // num_two
    elif operator == "add":
        results = num_one + num_two
    elif operator == "subtract":
        results = num_one - num_two

    return results


operator = input()
num_one = int(input())
num_two = int(input())
print(calculatioans(operator,num_one,num_two))