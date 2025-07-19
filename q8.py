import pandas as pd
import numpy as np
from scipy.stats import iqr

# Load dataset
df = pd.read_excel(r"lab2/Copy of Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")

# Copy to avoid modifying original
df_imputed = df.copy()

for col in df.columns:
    if df[col].isnull().any():
        if df[col].dtype in [np.float64, np.int64]:  # Numeric columns
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr_val = iqr(df[col].dropna())
            lower_bound = q1 - 1.5 * iqr_val
            upper_bound = q3 + 1.5 * iqr_val
            outliers_exist = df[col].dropna().apply(lambda x: x < lower_bound or x > upper_bound).any()

            if outliers_exist:
                # Use median for numeric columns with outliers
                median_val = df[col].median()
                df_imputed[col].fillna(median_val, inplace=True)
            else:
                # Use mean for numeric columns without outliers
                mean_val = df[col].mean()
                df_imputed[col].fillna(mean_val, inplace=True)
        else:
            # Use mode for categorical (object or string) columns
            mode_val = df[col].mode()[0]
            df_imputed[col].fillna(mode_val, inplace=True)

# Print to verify
print(df_imputed.isnull().sum())  # Should print 0 for all columns
