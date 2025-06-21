1) To coonect database local use sqlite3 ecommerce.db
.tables
.quit

Hybrid NLP-to-SQL ETL System
This project implements an intelligent, hybrid ETL (Extract, Transform, Load) pipeline that leverages a powerful natural language interface. It's designed to provide both high-speed analytics for common queries and the flexibility to query raw, detailed data when needed.

The core of the system is a one-time ETL process that runs on the application's first launch. It extracts and merges data from multiple source tables (customers, orders, products, etc.) into a single, clean summary table named final. For subsequent queries, the system uses Google's Gemini API to intelligently decide whether to query the fast, pre-joined final table or perform a new join on the original source tables if the requested data isn't available in the summary.

This hybrid approach ensures optimal performance for frequent requests while retaining the power to answer any question about the entire database.

Features
Intelligent Hybrid Querying: The AI automatically decides the most efficient query strategy—either using the fast summary table or joining the raw source tables.

One-Time ETL: Performs a comprehensive data merge and cleanup process only once to create a performance-optimized final table.

Natural Language Processing: Converts complex English questions into precise SQL queries.

Modular and Maintainable: The codebase is cleanly separated into modules for configuration, database utilities, NLP, and each ETL step (Extract, Transform, Load).

Serverless Database: Utilizes SQLite for a zero-installation, file-based database, making the project easy to set up and run anywhere.

Project Structure
The project is organized for clarity and maintainability:

final-etl-project/
├── config.py           # Stores API keys and database configuration.
├── db_utils.py         # Handles database connection, schema, and table checks.
├── nlp_to_sql.py       # Converts natural language queries to intelligent SQL.
├── extract.py          # Extracts data from the database.
├── transform.py        # Cleans and transforms the extracted data.
├── load.py             # Loads data into the final table.
├── main.py             # The main application entry point with hybrid logic.
├── requirements.txt    # Lists all Python dependencies.
├── init.sql            # SQL script to create and populate the source tables.
└── ecommerce.db        # The SQLite database file (created automatically).

Setup and Installation
Follow these steps to get the project running.

1. Prerequisites
Python 3.8 or newer.

DB Browser for SQLite (a free tool for managing the database file).

2. Clone or Download the Project
Ensure all the project files are located in a single directory on your machine.

3. Install Dependencies
Open your terminal, navigate to the project's root folder, and run:

pip install -r requirements.txt

4. Configure Your API Key
Open the config.py file.

Replace the placeholder text "YOUR_GEMINI_API_KEY_HERE" with your actual Gemini API key.

5. Create and Populate the Source Database (One-Time Setup)
This step creates your initial customers, products, etc., tables.

Run the Python script once:

python main.py

(The script will create an empty ecommerce.db file and warn you that the source tables are missing. This is the expected behavior.)

Open DB Browser for SQLite and click "Open Database". Select the ecommerce.db file from your project folder.

Go to the "Execute SQL" tab.

Click the "Open SQL file" icon and select your init.sql file.

Click the blue "Execute all" button (▶) to run the script.

Crucially, click the "Write Changes" button to save the tables and data, then you can close DB Browser.

How to Run the Application
With the setup complete, you can now run the system.

Navigate to your project directory in the terminal.

Execute the main script:

python main.py

On the first run, the application will detect that the final table is missing and will automatically perform the one-time ETL process to create it. On all subsequent runs, it will skip this step and be ready for your queries immediately.

How to Use
You can now ask the system any question. The AI will figure out the best way to get the answer.

Example 1: Fast Query (Uses the final table)
This query can be answered using the pre-joined summary table.

💬 Enter your query: Show all electronics products ordered by Alice Johnson

Example 2: Complex Query (Joins Source Tables)
Let's assume the payments table has data not included in the final table.

💬 Enter your query: what was the payment method for order 1001?

The AI will see that payment_method is not in the final table and will correctly generate a query that joins orders and payments to find the answer.

To exit the application, type quit or exit.
