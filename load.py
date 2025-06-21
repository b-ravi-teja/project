# load.py
# Loads the transformed data into a new database table.

def load_data(df, table_name, engine):
    """
    Loads the DataFrame into a specified table in the database.
    """
    if df is None or df.empty:
        print("✗ [Load] No data to load.")
        return

    print(f"\n🔄 [Load] Loading {len(df)} records into table '{table_name}'...")
    try:
        # if_exists='replace' will drop the table first if it exists and create a new one.
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"✓ [Load] Successfully loaded data into table '{table_name}'.")
    except Exception as e:
        print(f"✗ [Load] Error loading data: {e}")
