import numpy as np        # For numerical operations
import pandas as pd       # For handling datasets
import seaborn as sns     # For data visualization
import matplotlib.pyplot as plt  # For additional plotting features

# Generate a dataset with 100 random values
np.random.seed(42)  # Ensures reproducibility
data = np.random.randint(10, 100, 100)  # 100 random numbers between 10 and 100

# Convert it into a Pandas DataFrame
df = pd.DataFrame(data, columns=['Values'])

# Display the first few rows
print(df.head())

mean_value = df['Values'].mean()  # Compute mean
median_value = df['Values'].median()  # Compute median
mode_value = df['Values'].mode()[0]  # Compute mode (mode() returns a Series)
std_dev = df['Values'].std()  # Compute standard deviation
variance = df['Values'].var()  # Compute variance
range_value = df['Values'].max() - df['Values'].min()  # Compute range
q1 = df['Values'].quantile(0.25)  # Compute Q1 (25th percentile)
q3 = df['Values'].quantile(0.75)  # Compute Q3 (75th percentile)
iqr = q3 - q1  # Compute Interquartile Range (IQR)

# Print the computed values
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Range: {range_value}")
print(f"IQR: {iqr}")

# Histogram
plt.figure(figsize=(8,4))  # Set figure size
sns.histplot(df['Values'], bins=10, kde=True, color='blue')  # Create histogram with Kernel Density Estimate (KDE)
plt.title('Histogram of Values')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(6,3))
sns.boxplot(x=df['Values'], color='green')  # Create boxplot
plt.title('Boxplot of Values')
plt.show()

df['Z-Score'] = (df['Values'] - mean_value) / std_dev  # Compute Z-score

# Scatter plot of Z-scores
plt.figure(figsize=(8,4))
sns.scatterplot(x=range(len(df)), y=df['Z-Score'], color='red')
plt.axhline(y=0, color='black', linestyle='--')  # Mean reference line
plt.axhline(y=2, color='blue', linestyle='--', label='Z = 2')  # +2 SD
plt.axhline(y=-2, color='blue', linestyle='--', label='Z = -2')  # -2 SD
plt.legend()
plt.title('Z-Scores of Values')
plt.xlabel('Index')
plt.ylabel('Z-Score')
plt.show()

cv = (std_dev / mean_value) * 100
print(f"Coefficient of Variation: {cv:.2f}%")




