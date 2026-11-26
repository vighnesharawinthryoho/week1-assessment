import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    marks = np.array([
        [78, 85, 82],
        [65, 70, 68],
        [90, 88, 92],
        [72, 75, 70],
    ])
    print("=== NUMPY ===")
    print("Marks shape:", marks.shape)
    print("Student averages (axis=1):", np.mean(marks, axis=1))
    print("Subject averages (axis=0):", np.mean(marks, axis=0))

    grace_marks = marks + 5
    print("Marks after +5 grace (broadcasting):\n", grace_marks)

    weights = np.array([0.3, 0.3, 0.4])
    weighted_scores = np.dot(grace_marks, weights)
    print("Weighted scores (np.dot):", weighted_scores)

    print("\n=== PANDAS BASICS ===")
    df = pd.read_csv("employees.csv", encoding="utf-8-sig")
    print("Info:")
    print(df.info())
    print("\nDescribe:")
    print(df.describe(include="all"))
    print("\nloc (row 0, name & salary):\n", df.loc[0, ["name", "salary"]])
    print("\niloc (first 2 rows, first 3 cols):\n", df.iloc[:2, :3])
    print("\nFilter (salary >= 60000):\n", df[df["salary"] >= 60000])

    print("\n=== CLEANING & MERGE ===")
    dirty_df = df.copy()
    dirty_df.loc[1, "salary"] = np.nan
    dirty_df.loc[4, "salary"] = np.nan
    dirty_df = pd.concat([dirty_df, dirty_df.iloc[[0]]], ignore_index=True)

    print("Dirty shape (before cleaning):", dirty_df.shape)
    clean_df = dirty_df.drop_duplicates().copy()
    median_salary = clean_df["salary"].median()
    clean_df["salary"] = clean_df["salary"].fillna(median_salary).astype(int)
    clean_df["id"] = clean_df["id"].astype(int)
    print("Clean shape (after drop_duplicates & median fill):", clean_df.shape)
    print("Missing values after cleaning:\n", clean_df.isna().sum())

    dept_summary = (
        clean_df.groupby("department", as_index=False)["salary"]
        .agg(headcount="count", avg_salary="mean", max_salary="max")
    )
    print("\nGroupby aggregation:")
    print(dept_summary)

    dept_df = pd.read_csv("departments.csv", encoding="utf-8-sig")

    inner_merged = pd.merge(dept_summary, dept_df, on="department", how="inner")
    left_merged = pd.merge(dept_summary, dept_df, on="department", how="left")
    outer_merged = pd.merge(dept_summary, dept_df, on="department", how="outer")

    print("\nInner merge:\n", inner_merged)
    print("\nLeft merge:\n", left_merged)
    print("\nOuter merge:\n", outer_merged)

    no_emp_depts = outer_merged[outer_merged["headcount"].isna()]["department"].tolist()
    print("Departments with no employees (outer join):", no_emp_depts)

    plt.figure(figsize=(7, 4))
    plt.bar(dept_summary["department"], dept_summary["avg_salary"], color="steelblue", label="Avg Salary")
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart1_bar_dept_salary.png")
    plt.close()

    plt.figure(figsize=(7, 4))
    plt.hist(clean_df["salary"], bins=5, color="teal", edgecolor="black", label="Employee Count")
    plt.title("Employee Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart2_hist_salary.png")
    plt.close()

    plt.figure(figsize=(7, 4))
    plt.scatter(clean_df["id"], clean_df["salary"], color="darkorange", label="Employee Salary")
    plt.title("Salary by Employee ID")
    plt.xlabel("Employee ID")
    plt.ylabel("Salary")
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart3_scatter_id_salary.png")
    plt.close()

    students = ["S1", "S2", "S3", "S4"]
    plt.figure(figsize=(7, 4))
    plt.plot(students, weighted_scores, marker="o", color="purple", label="Weighted Score")
    plt.title("Student Weighted Scores")
    plt.xlabel("Student")
    plt.ylabel("Weighted Score")
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart4_line_student_scores.png")
    plt.close()

    print("\nSaved 4 PNG charts successfully.")


if __name__ == "__main__":
    main()
