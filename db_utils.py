# db_utils.py
# Handles database connection and schema retrieval for SQLite.

from sqlalchemy import create_engine, inspect
from config import DB_FILE # Import the database filename

def get_db_engine():
    """Creates and returns a SQLAlchemy database engine for SQLite."""
    try:
        connection_url = f"sqlite:///{DB_FILE}"
        engine = create_engine(connection_url)
        # This will create the file if it doesn't exist and test the connection.
        with engine.connect() as connection:
            print(f"✓ Database connection successful. Using file: {DB_FILE}")
        return engine
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return None

def get_database_schema(engine):
    """Retrieves the schema of the database to provide context to the AI."""
    try:
        inspector = inspect(engine)
        schema_info = "Database Schema:\n\n"
        table_names = inspector.get_table_names()
        
        if not table_names:
            return "Database is empty. You need to create tables and insert data first."

        for table_name in table_names:
            schema_info += f"Table: {table_name}\n"
            schema_info += "Columns: "
            columns = [col['name'] for col in inspector.get_columns(table_name)]
            schema_info += ", ".join(columns) + "\n\n"
        return schema_info
    except Exception as e:
        print(f"Could not inspect database schema: {e}")
        return "Error retrieving schema."
