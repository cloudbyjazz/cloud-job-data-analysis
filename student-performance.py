import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("students.csv")

# Show the full dataset
print("Student Data:")
print(df)

# Show average final grade
average_grade = df["FinalGrade"].mean()
print("\nAverage Final Grade:", round(average_grade, 2))

# Show highest grade
highest_grade = df["FinalGrade"].max()
print("Highest Final Grade:", highest_grade)

# Study hours vs final grade
plt.scatter(df["StudyHours"], df["FinalGrade"])
plt.title("Study Hours vs Final Grade")
plt.xlabel("Study Hours")
plt.ylabel("Final Grade")
plt.show()

# Attendance vs final grade
plt.bar(df["Name"], df["Attendance"])
plt.title("Student Attendance")
plt.xlabel("Student")
plt.ylabel("Attendance")
plt.show()
#New chart
plt.scatter(df["Attendance"], df["FinalGrade"])
plt.title("Attendance vs Final Grade")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Grade")
plt.show()