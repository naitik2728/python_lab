import pandas as pd

# Step 1: Read CSV file
file_name = "data.csv"

df = pd.read_csv(file_name)

# Step 2: Display dataset
print("Original Dataset:")
print(df)

# Step 3: Display dimensions
print("\nDataset Dimensions:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Step 4: Display data types
print("\nData Types:")
print(df.dtypes)

# Step 5: Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Step 6: Filter rows according to a condition
# Example: select rows where Age is greater than 18
filtered_df = df[df["Age"] > 18]

print("\nFiltered Data (Age > 18):")
print(filtered_df)

# Step 7: Save filtered data into a new CSV file
filtered_df.to_csv("filtered_data.csv", index=False)

print("\nFiltered data saved as 'filtered_data.csv'")