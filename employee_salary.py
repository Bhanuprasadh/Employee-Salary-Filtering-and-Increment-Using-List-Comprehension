employees = [
    ("Rahul", 45000),
    ("Priya", 55000),
    ("Arjun", 62000),
    ("Sneha", 48000),
    ("Kiran", 75000),
    ("Anita", 90000)
]

updated_employees = [
    (name, salary * 1.10)
    for name, salary in employees
    if salary > 50000
]

print("Employees receiving 10% salary increment:\n")

for name, salary in updated_employees:
    print(f"{name:<10} ₹{salary:,.2f}")