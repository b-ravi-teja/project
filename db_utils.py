# db_utils.py
# Handles database connection, schema retrieval, and table checks.

from sqlalchemy import create_engine, inspect
from config import DB_FILE

def get_db_engine():
    """Creates and returns a SQLAlchemy database engine for SQLite."""
    try:
        connection_url = f"sqlite:///{DB_FILE}"
        engine = create_engine(connection_url)
        with engine.connect() as connection:
            print(f"✓ Database connection successful. Using file: {DB_FILE}")
        return engine
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return None

def check_table_exists(engine, table_name):
    """Checks if a table exists in the database."""
    inspector = inspect(engine)
    return inspector.has_table(table_name)

def get_schema_for_prompt(engine):
    """
    Retrieves the schema for ALL tables to provide full context to the AI.
    It adds special instructions about how to use the 'final' table.
    """
    inspector = inspect(engine)
    schema_info = "You have the following tables in your SQLite database:\n\n"
    
    table_names = inspector.get_table_names()

    if not table_names:
        return "Database is empty. Please create tables first."

    # Describe each table
    for table_name in table_names:
        schema_info += f"--- Table: {table_name} ---\n"
        schema_info += "Columns: "
        columns = [col['name'] for col in inspector.get_columns(table_name)]
        schema_info += ", ".join(columns) + "\n"
        if table_name == 'final':
            schema_info += "Purpose: This is a pre-joined and cleaned summary table. PREFER using this table for common queries about customers, products, and orders for maximum speed.\n\n"
        else:
            schema_info += "Purpose: This is a raw source table. Use it only when the required information is NOT available in the 'final' table (e.g., for reviews, payments, etc.).\n\n"
            
    return schema_info
