# main.py
# Main application with one-time ETL and intelligent hybrid querying.

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
        print("📋 No records found for your query.")
        return
    print(f"\n📊 Query Results ({len(df)} records found):")
    print("=" * 80)
    with pd.option_context('display.max_rows', 20, 'display.max_columns', None, 'display.width', 120):
        print(df)
    if len(df) > 20:
        print(f"\n... and {len(df) - 20} more records.")

def perform_initial_etl(engine):
    """Performs a one-time ETL process to create the 'final' table."""
    print("\n🚀 Performing one-time initial ETL setup...")
    
    initial_extract_query = """
    SELECT
        c.name AS customer_name, c.email, c.phone, c.address,
        p.name AS product_name, p.category,
        oi.quantity, p.price AS unit_price, (oi.quantity * p.price) AS total_item_price,
        o.order_date,
        pm.payment_date, pm.method AS payment_method,
        d.delivery_status, d.delivery_date
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    LEFT JOIN payments pm ON o.order_id = pm.order_id
    LEFT JOIN delivery d ON o.order_id = d.order_id;
    """
    
    merged_df = extract.extract_data(initial_extract_query, engine)
    transformed_df = transform.transform_data(merged_df)
    load.load_data(transformed_df, 'final', engine)
    
    print("✅ Initial ETL setup complete. The 'final' table has been created.")

def run():
    """Runs the main interactive session."""
    print("🚀 Starting NLP-to-SQL Hybrid ETL System...")
    
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("✗ ERROR: Please set your GEMINI_API_KEY in the config.py file.")
        return

    engine = db_utils.get_db_engine()
    if not engine:
        return

    # --- ONE-TIME ETL CHECK ---
    if not db_utils.check_table_exists(engine, 'final'):
        source_tables = ['customers', 'products', 'orders', 'order_items']
        if not all(db_utils.check_table_exists(engine, t) for t in source_tables):
             print("\n✗ WARNING: Source tables not found. Please run your init.sql script first.")
             return
        perform_initial_etl(engine)

    # --- Main Query Loop ---
    print("\n✅ System is ready. Ask any question about your data.")
    print("-" * 60)
    
    # Always get the full schema to allow the AI to make intelligent choices
    full_schema = db_utils.get_schema_for_prompt(engine)

    while True:
        try:
            user_input = input("\n💬 Enter your query: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            if not user_input:
                continue
            
            print("\n🤖 Thinking and generating the most efficient SQL query...")
            sql_query = nlp_to_sql.convert_nlp_to_sql(user_input, full_schema)
            if not sql_query:
                continue

            results_df = extract.extract_data(sql_query, engine)
            display_results(results_df)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"✗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    run()
