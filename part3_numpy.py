import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df)

df['math_score'].fillna(df['math_score'].mean(), inplace=True)
df['science_score'].fillna(df['science_score'].mean(), inplace=True)
df['attendance'].fillna(df['attendance'].mean(), inplace=True)
df['gender'].fillna(df['gender'].mode()[0], inplace=True)

print("\nDataset after handling missing values:")
print(df)
df['math_score'] = pd.to_numeric(df['math_score'], errors='coerce')
df['science_score'] = pd.to_numeric(df['science_score'], errors='coerce')
df['exam_date'] = pd.to_datetime(df['exam_date'])

print("\nData Types after Conversion:")
print(df.dtypes)
Q1 = df['math_score'].quantile(0.25)
Q3 = df['math_score'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['math_score'] >= lower) & (df['math_score'] <= upper)]
print("\nDataset after Removing Outliers:")
print(df)
print("\nDuplicate Rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nDataset after Removing Duplicates:")
print(df)
