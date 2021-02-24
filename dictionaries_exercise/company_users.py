data = input()

company_info = {}
while not data == "End":
    company_name, employee = data.split(" -> ")
    if company_name not in company_info:
        company_info[company_name] = []
    if employee not in company_info[company_name]:
        company_info[company_name].append(employee)
    data = input()

sorted_company_info = dict(sorted(company_info.items()))
for company, employees in sorted_company_info.items():
    print(company)
    for employee_id in employees:
        print(f"-- {employee_id}")

