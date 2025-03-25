
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('sample_data.csv')  # Replace with your dataset

# Check missing values
print(df.isnull().sum())

# Clean: drop missing or fill
df = df.dropna()

# Convert date column (if exists)
# df['Date'] = pd.to_datetime(df['Date'])

# Visualization example
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()
