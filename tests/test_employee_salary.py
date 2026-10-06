from employee_salary import calculate_incremented_salaries


def test_eligible_employees_receive_increment():
    employees = [
        ("Rahul", 45000),
        ("Priya", 55000),
        ("Arjun", 62000),
    ]

    result = calculate_incremented_salaries(employees)

    assert result == [
        ("Priya", 60500),
        ("Arjun", 68200),
    ]


def test_salary_equal_to_threshold_is_not_eligible():
    employees = [
        ("Rahul", 50000),
    ]

    result = calculate_incremented_salaries(employees)

    assert result == []


def test_no_eligible_employees():
    employees = [
        ("Rahul", 40000),
        ("Priya", 50000),
    ]

    result = calculate_incremented_salaries(employees)

    assert result == []


def test_all_employees_are_eligible():
    employees = [
        ("Rahul", 60000),
        ("Priya", 70000),
    ]

    result = calculate_incremented_salaries(employees)

    assert result == [
        ("Rahul", 66000),
        ("Priya", 77000),
    ]


def test_empty_employee_list():
    result = calculate_incremented_salaries([])

    assert result == []