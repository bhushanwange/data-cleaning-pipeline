import pandas as pd

# 1. Import pandas and read the CSV file
print("Loading dataset...")
df = pd.read_csv("dataset.csv")
print("Original Data:\n", df)

# 2. Identify missing values and decide on imputation or removal
# Fill missing numeric salaries with the median salary, and missing text fields with 'Unknown'
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Department'] = df['Department'].fillna('Unknown')
df['Emp Name'] = df['Emp Name'].fillna('Not Provided')

# 3. Rename columns for clarity (remove spaces, standardize case)
df = df.rename(columns={
    'ID': 'employee_id',
    'Emp Name': 'employee_name',
    'Salary': 'salary',
    'Department': 'department'
})

print("\nCleaned Data:\n", df)

# 4. Export the cleaned DataFrame to a new CSV
df.to_csv("cleaned_dataset.csv", index=False)
print("\nSuccess! Cleaned dataset exported to 'cleaned_dataset.csv'.")