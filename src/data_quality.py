import pandas as pd


def check_data_quality(df):
    report = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "column_types": df.dtypes.astype(str).to_dict()
    }

    return report