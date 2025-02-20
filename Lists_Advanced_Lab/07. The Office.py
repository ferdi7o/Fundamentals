employees_happiness = input().split()
factorial = int(input())
happiness_employees = [int(item) * factorial for item in employees_happiness]

avarage_happiness = sum(happiness_employees) / len(happiness_employees)
happy_count = 0

for item in happiness_employees:
    if item >= avarage_happiness:
        happy_count += 1

if happy_count > (len(happiness_employees) / 2):
    print(f"Score: {happy_count}/{len(happiness_employees)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(happiness_employees)}. Employees are not happy!")