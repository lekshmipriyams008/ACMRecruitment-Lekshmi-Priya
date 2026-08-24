import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")


def show_missing(df, message):
    print(f"\n{message}:")
    print(df.isnull().sum())


def fill_missing_values(df):
    numerical_columns = df.select_dtypes(include="number").columns
    for column in numerical_columns:
        if df[column].isnull().sum() > 0:
            df[column] = df[column].fillna(df[column].median())

  
    categorical_columns = df.select_dtypes(include="object").columns
    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            df[column] = df[column].fillna(df[column].mode()[0])

    return df


def remove_duplicates(df):
    duplicates = df.duplicated().sum()
    print("\nDuplicate records before removal:", duplicates)

    df = df.drop_duplicates()

    print("Duplicate records after removal:", df.duplicated().sum())
    return df

print("Original dataset shape:", df.shape)

show_missing(df, "Missing values before cleaning")

df = fill_missing_values(df)

df = remove_duplicates(df)

show_missing(df, "Missing values after cleaning")

print("\nTotal missing values:", df.isnull().sum().sum())
print("Total duplicate records:", df.duplicated().sum())
print("Cleaned dataset shape:", df.shape)

df.to_csv("cleaned_students_performance.csv", index=False)

print("\nCleaned dataset saved successfully as:")
print("cleaned_students_performance.csv")
