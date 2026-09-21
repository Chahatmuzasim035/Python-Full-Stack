# ============================================================
# DAY 33 - MATPLOTLIB & DATA VISUALIZATION
# 100 Days of Python
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# PROGRAM 1: LINE PLOT
# ============================================================

def program_1_line_plot():
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    sales = [100, 150, 130, 180, 220]

    plt.plot(
        months,
        sales,
        color="blue",
        marker="o",
        linestyle="-",
        linewidth=2,
        label="Sales"
    )

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()
    plt.grid()
    plt.show()


# ============================================================
# PROGRAM 2: BAR CHART
# ============================================================

def program_2_bar_chart():
    departments = ["CSE", "ECE", "EEE", "ME"]
    students = [60, 45, 35, 30]

    plt.bar(
        departments,
        students,
        color="skyblue",
        edgecolor="black"
    )

    plt.title("Department Strength")
    plt.xlabel("Department")
    plt.ylabel("Number of Students")
    plt.show()


# ============================================================
# PROGRAM 3: HISTOGRAM
# ============================================================

def program_3_histogram():
    scores = [45, 50, 55, 60, 65, 70, 72, 75, 80, 85, 88, 90, 92, 95]

    plt.hist(
        scores,
        bins=5,
        color="orange",
        edgecolor="black"
    )

    plt.title("Exam Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()


# ============================================================
# PROGRAM 4: SCATTER PLOT
# ============================================================

def program_4_scatter_plot():
    study_hours = [1, 2, 3, 4, 5, 6, 7]
    marks = [45, 50, 58, 65, 70, 82, 90]

    plt.scatter(
        study_hours,
        marks,
        color="green",
        marker="o",
        s=80
    )

    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.grid()
    plt.show()


# ============================================================
# PROGRAM 5: PIE CHART
# ============================================================

def program_5_pie_chart():
    values = [40, 30, 20, 10]
    labels = ["Product A", "Product B", "Product C", "Product D"]

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Market Share")
    plt.show()


# ============================================================
# PROGRAM 6: BOX PLOT
# ============================================================

def program_6_box_plot():
    salaries = [
        25000,
        28000,
        30000,
        32000,
        35000,
        37000,
        40000,
        50000
    ]

    plt.boxplot(
        salaries,
        patch_artist=True,
        showmeans=True
    )

    plt.title("Salary Distribution")
    plt.ylabel("Salary")
    plt.show()


# ============================================================
# PROGRAM 7: AREA CHART
# ============================================================

def program_7_area_chart():
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    visitors = [100, 150, 180, 220, 300]

    plt.fill_between(
        months,
        visitors,
        alpha=0.5
    )

    plt.plot(months, visitors, marker="o")

    plt.title("Website Visitors")
    plt.xlabel("Month")
    plt.ylabel("Visitors")
    plt.show()


# ============================================================
# PROGRAM 8: BASIC HEATMAP
# ============================================================

def program_8_heatmap():
    data = [
        [80, 75, 90],
        [70, 85, 88],
        [92, 80, 95]
    ]

    sns.heatmap(
        data,
        annot=True,
        fmt="d",
        cmap="YlGnBu"
    )

    plt.title("Student Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Students")
    plt.show()


# ============================================================
# PROGRAM 9: HEATMAP USING DATAFRAME
# ============================================================

def program_9_dataframe_heatmap():
    data = [
        [80, 75, 90, 85],
        [70, 85, 88, 90],
        [92, 80, 95, 89]
    ]

    subjects = ["Python", "SQL", "Maths", "Statistics"]
    students = ["Student 1", "Student 2", "Student 3"]

    sns.heatmap(
        data,
        annot=True,
        fmt="d",
        cmap="coolwarm",
        xticklabels=subjects,
        yticklabels=students
    )

    plt.title("Student Performance")
    plt.show()


# ============================================================
# PROGRAM 10: TWO SUBPLOTS
# ============================================================

def program_10_subplots():
    months = ["Jan", "Feb", "Mar", "Apr"]
    sales = [100, 150, 130, 180]
    expenses = [70, 90, 85, 110]

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(months, sales, marker="o")
    plt.title("Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.subplot(1, 2, 2)
    plt.bar(months, expenses)
    plt.title("Expenses")
    plt.xlabel("Month")
    plt.ylabel("Expenses")

    plt.tight_layout()
    plt.show()


# ============================================================
# PROGRAM 11: SCATTER PLOT WITH DIFFERENT MARKER SIZE
# ============================================================

def program_11_scatter_customization():
    hours = [1, 2, 3, 4, 5, 6]
    marks = [40, 48, 55, 65, 75, 90]
    sizes = [50, 80, 100, 130, 160, 200]

    plt.scatter(
        hours,
        marks,
        s=sizes,
        color="purple",
        alpha=0.7
    )

    plt.title("Study Hours and Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.show()


# ============================================================
# PROGRAM 12: HISTOGRAM WITH DENSITY
# ============================================================

def program_12_histogram_density():
    data = [
        10, 12, 15, 15, 18,
        20, 22, 22, 25, 28,
        30, 32, 35, 35, 38
    ]

    plt.hist(
        data,
        bins=5,
        density=True,
        alpha=0.7,
        edgecolor="black"
    )

    plt.title("Data Distribution")
    plt.xlabel("Values")
    plt.ylabel("Density")
    plt.show()


# ============================================================
# PROGRAM 13: MULTIPLE LINE PLOTS
# ============================================================

def program_13_multiple_lines():
    months = ["Jan", "Feb", "Mar", "Apr", "May"]

    product_a = [100, 120, 150, 170, 200]
    product_b = [80, 110, 130, 160, 180]

    plt.plot(
        months,
        product_a,
        marker="o",
        label="Product A"
    )

    plt.plot(
        months,
        product_b,
        marker="s",
        label="Product B"
    )

    plt.title("Product Sales Comparison")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()
    plt.grid()
    plt.show()


# ============================================================
# PROGRAM 14: SALES DASHBOARD USING SUBPLOTS
# ============================================================

def program_14_sales_dashboard():
    months = ["Jan", "Feb", "Mar", "Apr"]

    sales = [100, 150, 130, 180]
    expenses = [70, 90, 85, 110]
    profit = [30, 60, 45, 70]

    plt.figure(figsize=(12, 8))

    # Line plot
    plt.subplot(2, 2, 1)
    plt.plot(months, sales, marker="o")
    plt.title("Sales")

    # Bar chart
    plt.subplot(2, 2, 2)
    plt.bar(months, expenses)
    plt.title("Expenses")

    # Area chart
    plt.subplot(2, 2, 3)
    plt.fill_between(months, profit, alpha=0.5)
    plt.plot(months, profit)
    plt.title("Profit")

    # Scatter plot
    plt.subplot(2, 2, 4)
    plt.scatter(months, sales)
    plt.title("Sales Scatter")

    plt.suptitle("Sales Dashboard")
    plt.tight_layout()
    plt.show()


# ============================================================
# PROGRAM 15: SAVE A CHART
# ============================================================

def program_15_save_chart():
    months = ["Jan", "Feb", "Mar", "Apr"]
    sales = [100, 150, 130, 180]

    plt.plot(
        months,
        sales,
        marker="o"
    )

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.savefig("monthly_sales.png")

    print("Chart saved as monthly_sales.png")

    plt.show()


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # Run programs one at a time by uncommenting them.

    program_1_line_plot()

    program_2_bar_chart()
    program_3_histogram()
    program_4_scatter_plot()
    program_5_pie_chart()
    program_6_box_plot()
    program_7_area_chart()
    program_8_heatmap()
    program_9_dataframe_heatmap()
    program_10_subplots()
    program_11_scatter_customization()
    program_12_histogram_density()
    program_13_multiple_lines()
    program_14_sales_dashboard()
    program_15_save_chart()