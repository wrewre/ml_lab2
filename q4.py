import pandas as pd
def analyze_excel_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)  # reading and processing file
    column_types = df.dtypes.to_dict()  # get types
    missing_values = df.isnull().sum().to_dict()  # count blanks
    categorical_columns = df.select_dtypes(include='object').columns  # finding the  words
    encoding_strategy = {}
    for col in categorical_columns:
        encoding_strategy[col] = 'One-Hot Encoding'  # marking for encode
    numeric_columns = df.select_dtypes(include='number').columns  # find numbers
    data_ranges = {}
    for col in numeric_columns:
        minimum = df[col].min()
        maximum = df[col].max()
        data_ranges[col] = (minimum, maximum)  # save min max
    stats = {}
    for col in numeric_columns:
        mean = df[col].mean()
        variance = df[col].var()
        stats[col] = {}
        stats[col]['Mean'] = round(mean, 2)
        stats[col]['Variance'] = round(variance, 2)  # mean and variance calcultion
    outlier_counts = {}
    for col in numeric_columns:
        quantiles = df[col].quantile([0.25, 0.75])
        q1 = quantiles.loc[0.25]
        q3 = quantiles.loc[0.75]
        iqr = q3 - q1
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr
        below_lower = df[col] < lower_limit
        above_upper = df[col] > upper_limit
        num_outliers = below_lower.sum() + above_upper.sum()
        outlier_counts[col] = num_outliers  # count odd values
    return column_types, encoding_strategy, data_ranges, missing_values, outlier_counts, stats

file_path = r"lab2/Copy of Lab Session Data.xlsx"
sheet_name = "thyroid0387_UCI"
column_types, encoding_strategy, data_ranges, missing_values, outlier_counts, stats = analyze_excel_data(file_path, sheet_name)

print("Data Types")
for col, dtype in column_types.items():
    print(f"{col}: {dtype}")  # show types

print("Encoding Suggestions")
for col, enc in encoding_strategy.items():
    print(f"{col}: {enc}")

print("Data Ranges")
for col, val in data_ranges.items():
    print(f"{col}: Min = {val[0]}, Max = {val[1]}")

print("Missing Values")
for col, count in missing_values.items():
    print(f"{col}: {count}")

print("Outlier Counts")
for col, count in outlier_counts.items():
    print(f"{col}: {count}")

print("Mean and Variance")
for col, values in stats.items():
    print(f"{col}: Mean = {values['Mean']}, Variance = {values['Variance']}")
