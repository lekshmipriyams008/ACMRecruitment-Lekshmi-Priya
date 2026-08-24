import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("Dataset loaded successfully!\n")

print("Dataset Shape:")
print(df.shape)

print("\nNumber of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn Names:")
for column in df.columns:
    print(column)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())
