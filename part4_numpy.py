import pandas as pd
df = pd.read_csv("students.csv")

df['average_score'] = (df['math_score'] + df['science_score']) / 2

print("Dataset with Average Score:")
print(df)

top_students = df.sort_values(by='average_score', ascending=False).head(5)

print("\nTop 5 Students:")
print(top_students)

correlation = df['attendance'].corr(df['average_score'])

print("\nCorrelation between Attendance and Average Score:")
print(correlation)

gender_average = df.groupby('gender')[['math_score',
                                       'science_score',
                                       'average_score']].mean()

print("\nAverage Marks by Gender:")
print(gender_average)
