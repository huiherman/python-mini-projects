
import pandas as pd

# Load CSV file
df = pd.read_csv('sample_data.csv')  # Replace with your CSV file

# Show first 5 rows
print(df.head())

# Show basic statistics
print(df.describe())

# Filter example: people older than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)
