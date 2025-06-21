# extract.py
# Executes the SQL query to extract data from the database.

import pandas as pd

def extract_data(sql_query, engine):
    """
    Executes the SQL query and returns the results as a pandas DataFrame.
    """
    if not sql_query or not sql_query.strip().upper().startswith('SELECT'):
        print("✗ [Extract] Invalid query. Only SELECT statements are allowed.")
        return None

    print(f"🔍 [Extract] Executing SQL: {sql_query}")
    try:
        df = pd.read_sql(sql_query, engine)
        print(f"✓ [Extract] Extracted {len(df)} records.")
        return df
    except Exception as e:
        print(f"✗ [Extract] Error executing SQL query: {e}")
        return None
