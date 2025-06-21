# transform.py
# Cleans and transforms the extracted data.

def transform_data(df):
    """
    Cleans the merged data.
    """
    if df is None or df.empty:
        print("✗ [Transform] No data to transform.")
        return df

    print("\n✨ [Transform] Starting data transformation...")
    rows_before = len(df)
    
    # Simple transformation: remove completely duplicate rows
    df.drop_duplicates(inplace=True)
    
    rows_after = len(df)
    removed_count = rows_before - rows_after
    
    if removed_count > 0:
        print(f"✓ [Transform] Removed {removed_count} duplicate records.")
    
    print("✓ [Transform] Transformation complete.")
    return df
