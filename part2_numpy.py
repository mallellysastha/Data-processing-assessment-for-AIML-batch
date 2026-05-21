import pandas as pd
df = pd.read_csv("students.csv")
print("First 5 Rows:")
print(df.head())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nStudents with Attendance below 70%:")
low_attendance = df[df['attendance'] < 70]
print(low_attendance)
