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