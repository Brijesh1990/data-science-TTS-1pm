# What is Pandas in Python?

Pandas is an open-source Python library that provides data structures and data analysis tools for working with structured data (tabular, time-series, and more). It's built on top of NumPy and is essential for data manipulation, cleaning, and analysis.

---

## Table of Contents
1. [Introduction & Installation](#introduction--installation)
2. [Core Data Structures](#core-data-structures)
3. [Creating DataFrames & Series](#creating-dataframes--series)
4. [Data Selection & Indexing](#data-selection--indexing)
5. [Data Cleaning & Manipulation](#data-cleaning--manipulation)
6. [Data Analysis & Aggregation](#data-analysis--aggregation)
7. [Data Grouping](#data-grouping)
8. [Merging & Joining Data](#merging--joining-data)
9. [File I/O Operations](#file-io-operations)
10. [Time Series Data](#time-series-data)

---

## Introduction & Installation

### What is Pandas?
Pandas stands for "Python Data Analysis Library" and is used for:
- Data cleaning and preparation
- Data manipulation and transformation
- Data analysis and exploration
- Statistical operations
- Handling missing data

### Installation
```bash
pip install pandas
```

### Import Pandas
```python
import pandas as pd
```

---

## Core Data Structures

### 1. Series
A one-dimensional labeled array with index and values.

```python
import pandas as pd

# Create a Series from a list
s = pd.Series([10, 20, 30, 40])
print(s)
# Output:
# 0    10
# 1    20
# 2    30
# 3    40

# Create a Series with custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# Output:
# a    10
# b    20
# c    30

# Create a Series from a dictionary
s = pd.Series({'name': 'John', 'age': 25, 'city': 'NYC'})
print(s)
```

### 2. DataFrame
A two-dimensional labeled data structure with rows and columns.

```python
import pandas as pd

# Create a DataFrame from a dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
})
print(df)
```

---

## Creating DataFrames & Series

### From Lists
```python
import pandas as pd

# From list of lists
df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
print(df)
```

### From Dictionaries
```python
# From dictionary
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)
```

### From NumPy Arrays
```python
import numpy as np
import pandas as pd

arr = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(arr, columns=['X', 'Y'])
print(df)
```

### From CSV File
```python
df = pd.read_csv('data.csv')
print(df.head())
```

### From Excel File
```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(df)
```

### From JSON File
```python
df = pd.read_json('data.json')
print(df)
```

---

## Data Selection & Indexing

### Column Selection
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
})

# Select single column
print(df['Name'])

# Select multiple columns
print(df[['Name', 'Age']])
```

### Row Selection
```python
# Select by position (iloc)
print(df.iloc[0])  # First row
print(df.iloc[0:2])  # First two rows

# Select by label (loc)
print(df.loc[0])  # Row with index 0
print(df.loc[0:1])  # Rows with index 0 to 1
```

### Conditional Selection
```python
# Select rows where Age > 25
print(df[df['Age'] > 25])

# Select rows with multiple conditions
print(df[(df['Age'] > 25) & (df['Salary'] > 55000)])

# Using isin()
print(df[df['Name'].isin(['Alice', 'Bob'])])
```

### Using at and iat
```python
# Get single value by label
print(df.at[0, 'Name'])  # Returns 'Alice'

# Get single value by position
print(df.iat[0, 0])  # Returns 'Alice'
```

---

## Data Cleaning & Manipulation

### Handling Missing Data
```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, 12]
})

# Check for missing values
print(df.isnull())
print(df.isna())

# Count missing values
print(df.isnull().sum())

# Drop rows with missing values
print(df.dropna())

# Drop columns with missing values
print(df.dropna(axis=1))

# Fill missing values
print(df.fillna(0))  # Fill with 0
print(df.fillna(method='ffill'))  # Forward fill
print(df.fillna(method='bfill'))  # Backward fill

# Fill with different values per column
print(df.fillna({'A': 0, 'B': 99}))
```

### Data Type Conversion
```python
import pandas as pd

df = pd.DataFrame({
    'Age': ['25', '30', '35'],
    'Salary': ['50000', '60000', '70000']
})

# Convert to numeric
df['Age'] = pd.to_numeric(df['Age'])
df['Salary'] = pd.to_numeric(df['Salary'])

# Convert to string
df['Age'] = df['Age'].astype(str)

# Convert to category
df['Age'] = df['Age'].astype('category')

# Check data types
print(df.dtypes)
```

### Renaming Columns
```python
# Rename single column
df = df.rename(columns={'Age': 'Years'})

# Rename multiple columns
df = df.rename(columns={'Name': 'Full_Name', 'Age': 'Years'})

# In-place rename
df.rename(columns={'Age': 'Years'}, inplace=True)
```

### Dropping Rows & Columns
```python
# Drop specific columns
df = df.drop(columns=['Age', 'Salary'])
df = df.drop(['Age', 'Salary'], axis=1)

# Drop specific rows
df = df.drop([0, 2])  # Drop rows with index 0 and 2
df = df.drop(df.index[0:2])  # Drop first two rows

# Drop duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset=['Name'])
```

### String Operations
```python
import pandas as pd

df = pd.DataFrame({'Name': ['alice', 'bob', 'charlie']})

# Convert to uppercase
df['Name'] = df['Name'].str.upper()

# Convert to lowercase
df['Name'] = df['Name'].str.lower()

# Capitalize
df['Name'] = df['Name'].str.capitalize()

# String length
df['Name_Length'] = df['Name'].str.len()

# String contains
print(df[df['Name'].str.contains('a')])

# String split
df[['First', 'Last']] = df['Name'].str.split(' ', expand=True)

# String replace
df['Name'] = df['Name'].str.replace('a', 'X')
```

---

## Data Analysis & Aggregation

### Basic Statistics
```python
import pandas as pd

df = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})

# Descriptive statistics
print(df.describe())

# Mean
print(df.mean())
print(df['Age'].mean())

# Median
print(df.median())

# Standard deviation
print(df.std())

# Min and Max
print(df.min())
print(df.max())

# Sum
print(df.sum())

# Count
print(df.count())

# Correlation
print(df.corr())

# Variance
print(df.var())
```

### Sorting
```python
# Sort by single column
df_sorted = df.sort_values(by='Age')

# Sort by multiple columns
df_sorted = df.sort_values(by=['Age', 'Salary'])

# Sort in descending order
df_sorted = df.sort_values(by='Age', ascending=False)

# Sort by index
df_sorted = df.sort_index()

# In-place sorting
df.sort_values(by='Age', inplace=True)
```

### Ranking
```python
# Rank values
df['Age_Rank'] = df['Age'].rank()

# Rank in ascending order
df['Age_Rank'] = df['Age'].rank(ascending=True)
```

### Unique & Value Counts
```python
# Get unique values
print(df['Department'].unique())

# Count unique values
print(df['Department'].nunique())

# Value counts
print(df['Department'].value_counts())

# Value counts with percentages
print(df['Department'].value_counts(normalize=True))
```

---

## Data Grouping

### GroupBy Operations
```python
import pandas as pd

df = pd.DataFrame({
    'Department': ['Sales', 'IT', 'Sales', 'IT', 'HR'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 55000, 65000, 48000]
})

# Group by single column
grouped = df.groupby('Department')

# Get first row of each group
print(grouped.first())

# Get group size
print(grouped.size())

# Aggregate by sum
print(grouped['Salary'].sum())

# Aggregate by multiple functions
print(grouped['Salary'].agg(['sum', 'mean', 'count']))

# Aggregate multiple columns
print(grouped.agg({'Salary': 'sum', 'Name': 'count'}))

# Custom aggregation function
def custom_agg(x):
    return x.max() - x.min()

print(grouped['Salary'].agg(custom_agg))

# Group by multiple columns
grouped = df.groupby(['Department', 'Name'])
print(grouped.sum())
```

### Transform
```python
# Add group statistics to original DataFrame
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
print(df)

# Normalize within groups
df['Normalized_Salary'] = df.groupby('Department')['Salary'].transform(lambda x: (x - x.mean()) / x.std())
```

---

## Merging & Joining Data

### Merge (SQL-like Join)
```python
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Salary': [50000, 60000, 70000]
})

# Inner join (default)
merged = pd.merge(df1, df2, on='ID')
print(merged)

# Left join
merged = pd.merge(df1, df2, on='ID', how='left')

# Right join
merged = pd.merge(df1, df2, on='ID', how='right')

# Outer join
merged = pd.merge(df1, df2, on='ID', how='outer')

# Merge on different column names
merged = pd.merge(df1, df2, left_on='ID', right_on='ID')
```

### Concatenate
```python
import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
})

# Concatenate rows
result = pd.concat([df1, df2])  # axis=0 (default)

# Concatenate columns
result = pd.concat([df1, df2], axis=1)

# Ignore index
result = pd.concat([df1, df2], ignore_index=True)
```

### Join
```python
# Join on index
df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')
joined = df1_indexed.join(df2_indexed)
print(joined)
```

---

## File I/O Operations

### Reading Data
```python
import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Read with specific parameters
df = pd.read_csv('data.csv', sep=';', encoding='utf-8', nrows=100)

# Read Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Read JSON
df = pd.read_json('data.json')

# Read SQL
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///database.db')
df = pd.read_sql('SELECT * FROM table_name', engine)

# Read HTML
df = pd.read_html('https://example.com')[0]

# Read Parquet
df = pd.read_parquet('data.parquet')
```

### Writing Data
```python
# Write to CSV
df.to_csv('output.csv', index=False)

# Write to Excel
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# Write to JSON
df.to_json('output.json')

# Write to SQL
df.to_sql('table_name', engine, if_exists='replace')

# Write to Parquet
df.to_parquet('output.parquet')

# Write to HTML
df.to_html('output.html')
```

---

## Time Series Data

### Creating Time Series
```python
import pandas as pd

# Create date range
dates = pd.date_range('2023-01-01', periods=5, freq='D')
df = pd.DataFrame({'Date': dates, 'Value': [10, 20, 30, 40, 50]})

# Set Date as index
df = df.set_index('Date')

# Create time series from string
df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Value': [10, 20, 30]
})
df['Date'] = pd.to_datetime(df['Date'])
```

### Time-based Indexing
```python
# Select data by date
print(df['2023-01-01'])

# Select date range
print(df['2023-01-01':'2023-01-03'])

# Extract time components
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day
```

### Resampling
```python
# Downsample to weekly data
weekly = df.resample('W').sum()

# Downsample to monthly
monthly = df.resample('M').mean()

# Upsample to hourly
hourly = df.resample('H').ffill()

# Custom resampling rule
custom = df.resample('3D').sum()  # Every 3 days
```

### Rolling Window
```python
# Rolling mean (window of 3)
df['Rolling_Mean'] = df['Value'].rolling(window=3).mean()

# Rolling sum
df['Rolling_Sum'] = df['Value'].rolling(window=2).sum()

# Expanding window
df['Expanding_Mean'] = df['Value'].expanding().mean()
```

---

## Advanced Topics

### Apply and Map
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Apply function to column
df['Age_Category'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Old')

# Apply function to entire row
df['Info'] = df.apply(lambda row: f"{row['Name']} is {row['Age']}", axis=1)

# Map values
age_map = {25: 'Twenty-five', 30: 'Thirty', 35: 'Thirty-five'}
df['Age_Word'] = df['Age'].map(age_map)
```

### Pivot Tables
```python
import pandas as pd

df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 250]
})

# Create pivot table
pivot = pd.pivot_table(df, values='Sales', index='Date', columns='Category', aggfunc='sum')
print(pivot)
```

### Cross Tabulation
```python
import pandas as pd

df = pd.DataFrame({
    'A': ['one', 'one', 'one', 'two', 'two', 'two'],
    'B': ['foo', 'foo', 'bar', 'foo', 'foo', 'bar'],
    'C': [1, 2, 3, 4, 5, 6]
})

# Cross tabulation
crosstab = pd.crosstab(df['A'], df['B'])
print(crosstab)
```

### Query Method
```python
import pandas as pd

df = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})

# Query data
result = df.query('Age > 30 and Salary > 55000')
print(result)
```

### Categorical Data
```python
import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C', 'B']
})

# Convert to category
df['Category'] = df['Category'].astype('category')

# Get categories
print(df['Category'].cat.categories)

# Rename categories
df['Category'] = df['Category'].cat.rename_categories(['X', 'Y', 'Z'])
```

---

## Performance Tips

1. **Use vectorized operations** instead of loops
2. **Avoid chained indexing** - use `loc` or `iloc` properly
3. **Use `inplace=True`** to modify DataFrames without creating copies
4. **Use `copy()` when needed** to avoid SettingWithCopyWarning
5. **Use `.loc` for label-based indexing** and `.iloc` for position-based indexing
6. **Use categorical data** for columns with limited unique values
7. **Use `eval()` and `query()`** for complex filtering operations
8. **Chunk large files** when reading
9. **Delete unnecessary columns** to save memory
10. **Use appropriate data types** to reduce memory usage

---

## Summary

Pandas is a powerful library for data manipulation and analysis in Python. The main advantages include:

- Easy handling of missing data
- Flexible data structures (Series and DataFrames)
- Powerful data grouping and aggregation
- Built-in statistical functions
- Integration with other libraries like NumPy, Matplotlib, and Scikit-learn
- Support for multiple file formats
- Excellent performance with large datasets

By mastering pandas, you can efficiently clean, transform, and analyze data for data science and business intelligence projects.
