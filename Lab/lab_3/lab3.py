employees = []
for i in range(5):
    name = input(f"Enter name of employee {i+1}: ")
    salary = float(input(f"Enter salary of {name}: "))
    employees.append((name, salary))

print("\nEmployee Classification:")
print("-" * 30)

for name, salary in employees:
    if salary < 20000:
        emp_class = "C Class"
    elif salary < 60000:
        emp_class = "B Class"
    elif salary < 100000:
        emp_class = "A Class"
    else:
        emp_class = "Top Class"

    print(f"{name}: {emp_class} (Salary: {salary})")
