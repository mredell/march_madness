import os
import pandas as pd

def infer_sqlalchemy_types(df):
    """Infer SQLAlchemy column types from a Pandas DataFrame."""
    from sqlalchemy.types import Integer, Float, String, Date

    type_mapping = {}
    for col in df.columns:
        if pd.api.types.is_integer_dtype(df[col]):
            type_mapping[col] = Integer
        elif pd.api.types.is_float_dtype(df[col]):
            type_mapping[col] = Float
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            type_mapping[col] = Date
        else:
            type_mapping[col] = String  # Default to TEXT
    return type_mapping

def process_csv_folder(folder_path, engine):
    """Iterate over CSVs in a folder and import them as tables."""
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            table_name = os.path.splitext(filename)[0]  # Table name = filename (without .csv)

            print(f"📂 Processing {filename} → Table: {table_name}")

            # Read CSV into Pandas DataFrame
            df = pd.read_csv(file_path, encoding="cp1252")

            # Convert possible date columns
            for col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col], format="%m/%d/%Y")  # Try to convert date columns
                except (ValueError, TypeError):
                    pass  # Ignore if not convertible

            # Infer data types
            dtype_mapping = infer_sqlalchemy_types(df)

            # Import CSV into PostgreSQL
            df.to_sql(table_name, engine, schema="raw", if_exists="replace", index=False, dtype=dtype_mapping)

            print(f"✅ Imported {filename} into PostgreSQL as {table_name}\n")
    pass