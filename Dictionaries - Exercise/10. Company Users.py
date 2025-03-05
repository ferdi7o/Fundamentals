all_companies = {}

while True:
    company = input()
    if company == "End":
        break

    name_of_company, employee_id = company.split(" -> ")
    if name_of_company not in all_companies.keys():
        all_companies[name_of_company] = [employee_id]
    else:
        if employee_id in all_companies[name_of_company]:
            continue
        all_companies[name_of_company].append(employee_id)

for company_name in all_companies.keys():
    print(f"{company_name}")
    for id in all_companies[company_name]:
        print(f"-- {id}")