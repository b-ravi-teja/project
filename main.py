# main.py
# The main application file to run the NLP-to-SQL ETL process.

from config import GEMINI_API_KEY
import db_utils
import nlp_to_sql
import extract
import transform
import load
import pandas as pd

def display_results(df):
    """A helper function to display DataFrame results neatly."""
    if df is None or df.empty:
        print("📋 No records to display.")
        return
    print(f"\n📊 Query Results ({len(df)} records found):")
    print("=" * 80)
    with pd.option_context('display.max_rows', 20, 'display.max_columns', None, 'display.width', 120):
        print(df)
    if len(df) > 20:
        print(f"\n... and {len(df) - 20} more records.")

def run():
    """Runs the main interactive session."""
    print("🚀 Starting NLP-to-SQL ETL System...")
    
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("✗ ERROR: Please set your GEMINI_API_KEY in the config.py file.")
        return

    # 1. Connect to the database
    engine = db_utils.get_db_engine()
    if not engine:
        return

    # 2. Get the database schema for AI context
    schema = db_utils.get_database_schema(engine)
    if "Database is empty" in schema:
        print(f"\n✗ WARNING: {schema}")
        print("  Please run your init.sql script using a DB Browser to create tables.")
        return

    print("\n✅ System is ready. Ask questions that require merging tables.")
    print("   Example: 'Show me all products ordered by Alice Johnson'")
    print("   Type 'quit' or 'exit' to end the session.")
    print("-" * 60)

    while True:
        try:
            user_input = input("\n💬 Enter your query: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            if not user_input:
                continue
            
            # --- NLP to SQL Step ---
            print("\n🤖 Converting natural language to SQL...")
            sql_query = nlp_to_sql.convert_nlp_to_sql(user_input, schema)
            if not sql_query:
                continue

            # --- EXTRACT Step ---
            extracted_df = extract.extract_data(sql_query, engine)
            
            if extracted_df is None or extracted_df.empty:
                display_results(extracted_df) # Will print "No records found"
                continue

            # --- TRANSFORM Step ---
            transformed_df = transform.transform_data(extracted_df)
            print("\nData after cleaning and transformation:")
            display_results(transformed_df)

            # --- LOAD Step (as per professor's instructions) ---
            final_table_name = "final"
            print(f"\nAs per requirements, loading this data into the '{final_table_name}' table.")
            load.load_data(transformed_df, final_table_name, engine)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"✗ An unexpected error occurred in the main loop: {e}")

if __name__ == "__main__":
    run()
