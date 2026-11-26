import csv

def bonus(salary, rate=0.1, *extras, **options):
    total = salary * rate + sum(extras)
    if "cap" in options and total > options["cap"]:
        total = options["cap"]
    return total

class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Monthly Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"Manager: {self.name}, Monthly Salary: {self.salary}, Team Size: {self.team_size}"

if __name__ == "__main__":
    print("Bonus default:", bonus(50000))
    print("Bonus with extras:", bonus(50000, 0.1, 2000, 1500))
    print("Bonus capped:", bonus(50000, 0.1, 2000, 1500, cap=7000))

    emp = Employee("Arun", 30000)
    mgr = Manager("Divya", 75000, 6)
    print(emp.get_details(), "| Annual:", emp.annual_salary())
    print(mgr.get_details(), "| Annual:", mgr.annual_salary())

    try:
        bad_emp = Employee("Invalid", -500)
    except InvalidSalaryError as e:
        print(f"Error: {e}")
    finally:
        print("Transaction finished")

    with open("employees.csv", mode="r", encoding="utf-8-sig", newline="") as f:
        employees = [
            {
                "id": int(row["id"]),
                "name": row["name"],
                "department": row["department"],
                "salary": int(row["salary"]),
                "city": row["city"],
            }
            for row in csv.DictReader(f)
        ]

    above_50000 = [e["name"] for e in employees if e["salary"] > 50000]
    raised = list(map(lambda e: {**e, "salary": round(e["salary"] * 1.1, 2)}, employees))
    chennai = [e["name"] for e in filter(lambda e: e["city"] == "Chennai", employees)]

    print("Above 50000:", above_50000)
    print("Chennai:", chennai)
    print("10% raise:", [(e["name"], e["salary"]) for e in raised])

    loop_salaries = [0, 30000, 60000, 0, 90000, 52000]
    selected = []
    for sal in loop_salaries:
        if sal == 0:
            continue
        selected.append(sal)
        if sal > 85000:
            break
    print("Loop salaries (continue/break):", selected)
