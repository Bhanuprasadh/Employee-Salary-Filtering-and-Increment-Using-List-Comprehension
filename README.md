# Employee Salary Filtering and Increment Using List Comprehension

## 📌 Project Overview

This project demonstrates the use of **Python list comprehension** to filter and transform employee salary data.

The HR department of an Indian IT company wants to identify employees whose salary is **greater than ₹50,000** and provide them with a **10% salary increment**.

The project filters eligible employees, calculates their revised salaries, and stores the results in a new list using Python list comprehension.

---

## 🎯 Problem Statement

Given a list of employees and their salaries:

- Select employees whose salary is greater than ₹50,000.
- Increase the salary of each eligible employee by 10%.
- Store the updated employee information in a new list.
- Implement the operation using Python list comprehension.

---

## 🎯 Objectives

- Understand and implement Python list comprehension.
- Filter employee records based on a salary condition.
- Apply a 10% salary increment to eligible employees.
- Generate a new list without modifying the original employee data.
- Implement reusable and testable Python code.
- Perform automated testing using `pytest`.
- Analyse the time and space complexity of the solution.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13+ | Core programming language |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Source code repository |

No external libraries are required for the core application.

---

## 📂 Project Structure

```text
employee-salary-project-CTP/
│
├── tests/
│   ├── __init__.py
│   └── test_employee_salary.py
│
├── .gitignore
├── README.md
├── employee_salary.py
└── requirements.txt
```

> The `.venv/` directory is created locally but is excluded from Git using `.gitignore`.

---

## 📊 Input Data

The project uses the following sample employee data:

```python
employees = [
    ("Rahul", 45_000),
    ("Priya", 55_000),
    ("Arjun", 62_000),
    ("Sneha", 48_000),
    ("Kiran", 75_000),
    ("Anita", 90_000),
]
```

Each employee is represented as:

```text
(employee_name, salary)
```

---

## ⚙️ Working Principle

The program performs the following operations:

```text
Employee Data
     │
     ▼
Check Salary > ₹50,000
     │
     ├── No ──────► Exclude Employee
     │
     └── Yes
          │
          ▼
   Apply 10% Increment
          │
          ▼
   Store in New List
          │
          ▼
     Display Result
```

The list comprehension performs three operations:

1. **Iteration** — processes every employee.
2. **Filtering** — selects employees whose salary is greater than ₹50,000.
3. **Transformation** — increases the salary by 10%.

---

## 💻 Implementation

The main salary calculation is implemented using list comprehension:

```python
return [
    (name, round(salary * (1 + increment), 2))
    for name, salary in employees
    if salary > threshold
]
```

### Complete Implementation

```python
"""Employee salary filtering and increment using list comprehension."""


def calculate_incremented_salaries(
    employees: list[tuple[str, float]],
    threshold: float = 50_000,
    increment: float = 0.10,
) -> list[tuple[str, float]]:
    """Return eligible employees with their incremented salaries."""
    return [
        (name, round(salary * (1 + increment), 2))
        for name, salary in employees
        if salary > threshold
    ]


def main() -> None:
    employees = [
        ("Rahul", 45_000),
        ("Priya", 55_000),
        ("Arjun", 62_000),
        ("Sneha", 48_000),
        ("Kiran", 75_000),
        ("Anita", 90_000),
    ]

    updated_employees = calculate_incremented_salaries(employees)

    print("Employees receiving 10% salary increment:\n")

    for name, salary in updated_employees:
        print(f"{name:<10} ₹{salary:,.2f}")


if __name__ == "__main__":
    main()
```

---

## 🔍 Understanding the List Comprehension

The core expression is:

```python
[
    (name, round(salary * (1 + increment), 2))
    for name, salary in employees
    if salary > threshold
]
```

It can be understood as:

### 1. Iteration

```python
for name, salary in employees
```

Processes every employee in the input list.

### 2. Filtering

```python
if salary > threshold
```

Selects only employees whose salary is greater than ₹50,000.

### 3. Transformation

```python
salary * (1 + increment)
```

For a 10% increment:

```text
salary × 1.10
```

For example:

```text
₹55,000 × 1.10 = ₹60,500
```

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Bhanuprasadh/Employee-Salary-Filtering-and-Increment-Using-List-Comprehension.git
```

### 2. Navigate to the Project

```bash
cd Employee-Salary-Filtering-and-Increment-Using-List-Comprehension
```

### 3. Create a Virtual Environment

macOS/Linux:

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

macOS/Linux:

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run:

```bash
python employee_salary.py
```

### Expected Output

```text
Employees receiving 10% salary increment:

Priya      ₹60,500.00
Arjun      ₹68,200.00
Kiran      ₹82,500.00
Anita      ₹99,000.00
```

---

## 🧪 Testing

The project includes automated tests using **pytest**.

Run all tests with:

```bash
pytest
```

The test suite verifies:

- Eligible employees receive the correct increment.
- Employees earning exactly ₹50,000 are not selected.
- No eligible employees are handled correctly.
- All employees being eligible is handled correctly.
- An empty employee list is handled correctly.
- Salary calculations are correct.

### Expected Test Result

```text
============================= test session starts =============================
collected 5 items

tests/test_employee_salary.py .....                                      [100%]

============================== 5 passed =======================================
```

---

## 🧩 Test Cases

| Test Case | Expected Behaviour |
|---|---|
| Salary > ₹50,000 | Employee receives 10% increment |
| Salary = ₹50,000 | Employee is not selected |
| Salary < ₹50,000 | Employee is not selected |
| No eligible employees | Returns an empty list |
| All employees eligible | All receive the increment |
| Empty input | Returns an empty list |

---

## ⚠️ Important Boundary Condition

The requirement states that the salary must be **greater than ₹50,000**.

Therefore:

```text
₹49,999 → Not eligible
₹50,000 → Not eligible
₹50,001 → Eligible
```

The implementation correctly uses:

```python
if salary > threshold
```

and not:

```python
if salary >= threshold
```

---

## 💰 Floating-Point Precision

Salary calculations use rounding to two decimal places:

```python
round(salary * (1 + increment), 2)
```

This prevents small floating-point representation issues such as:

```text
60500.00000000001
```

and produces:

```text
60500.00
```

This is particularly useful when displaying monetary values.

---

## 📈 Complexity Analysis

### Time Complexity

```text
O(n)
```

Each employee is processed once.

Where:

```text
n = number of employees
```

### Space Complexity

```text
O(k)
```

Where:

```text
k = number of eligible employees
```

The program creates a new list containing only employees who satisfy the salary condition.

### Worst-Case Space Complexity

```text
O(n)
```

If every employee has a salary greater than ₹50,000, the result list will contain all employees.

---

## 🔄 Traditional Loop vs List Comprehension

### Traditional Approach

```python
result = []

for name, salary in employees:
    if salary > 50_000:
        result.append((name, salary * 1.10))
```

### List Comprehension

```python
result = [
    (name, salary * 1.10)
    for name, salary in employees
    if salary > 50_000
]
```

### Advantages of List Comprehension

- Concise syntax.
- Easy to read for simple operations.
- Combines filtering and transformation.
- Creates a new list directly.
- Well suited for this problem.

A traditional loop may be preferable when the processing logic becomes more complex.

---

## 🧠 Algorithm

1. Start.
2. Create the employee list containing names and salaries.
3. Set the salary eligibility threshold to ₹50,000.
4. Set the salary increment to 10%.
5. Iterate through each employee using list comprehension.
6. Check whether the salary is greater than ₹50,000.
7. If eligible, calculate the new salary using a 10% increment.
8. Store the employee name and updated salary in a new list.
9. Display the updated employee salaries.
10. Stop.

---

## 📋 Sample Result

| Employee | Original Salary | Eligibility | Updated Salary |
|---|---:|:---:|---:|
| Rahul | ₹45,000 | ❌ No | — |
| Priya | ₹55,000 | ✅ Yes | ₹60,500 |
| Arjun | ₹62,000 | ✅ Yes | ₹68,200 |
| Sneha | ₹48,000 | ❌ No | — |
| Kiran | ₹75,000 | ✅ Yes | ₹82,500 |
| Anita | ₹90,000 | ✅ Yes | ₹99,000 |

---

## 🌐 Real-World Applications

The same approach can be applied to:

- Employee salary revision.
- Performance-based salary increments.
- Employee bonus eligibility.
- HR data filtering.
- Incentive calculation.
- Financial data processing.
- Employee benefits eligibility.
- Dataset filtering and transformation.

---

## 🔮 Future Enhancements

The project can be extended by:

- Reading employee information from CSV files.
- Accepting employee data through user input.
- Storing employee records in a database.
- Supporting different increment percentages.
- Generating salary revision reports.
- Adding employee IDs and departments.
- Adding a graphical user interface.
- Developing a web-based HR salary management application.

These enhancements are outside the scope of the current academic requirement.

---

## 📌 Result

The project successfully filters employees whose salary is greater than ₹50,000 and applies a 10% salary increment using Python list comprehension.

The solution demonstrates:

- List comprehension
- Conditional filtering
- Data transformation
- Functions
- Type hints
- Automated testing
- Floating-point handling
- Time and space complexity analysis

The implementation is concise, reusable, testable and efficient for the given problem.

---

## 👨‍💻 Author

**Bhanuprasadh Santra**

M.Tech – Artificial Intelligence & Machine Learning

---

## 📄 Academic Project

**Project:** Employee Salary Filtering and Increment Using List Comprehension

**Subject:** Computational Thinking and Programming

**Type:** Academic Mini Project