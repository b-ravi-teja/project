1) To coonect database local use sqlite3 ecommerce.db
.tables
.quit

# NLP-to-SQL ETL System

This project is a sophisticated ETL (Extract, Transform, Load) pipeline that translates natural language questions into SQL queries, executes them on a database, cleans the resulting data, and loads it into a final summary table. It's designed to provide a powerful yet user-friendly interface for data analysis without requiring the user to write complex SQL.

The system is built with a modular architecture, making it easy to understand, maintain, and extend. It uses Google's Gemini API for state-of-the-art natural language processing and a local SQLite database for easy setup and portability.

---

## Features

-   **Natural Language Processing**: Converts plain English questions (e.g., "show all laptops ordered by Alice") into executable SQL queries.
-   **Automated ETL Pipeline**: Implements a full Extract, Transform, and Load process.
-   **Modular Codebase**: Each major function (extract, transform, load, NLP, DB utils) is separated into its own module for clean and maintainable code.
-   **Local Database**: Uses SQLite for a serverless, zero-installation database setup, making the project highly portable.
-   **Dynamic Reporting**: Automatically merges data from multiple tables based on the user's query and loads the result into a final report table named `final`.

---

## Project Structure

The project is organized into several modules, each with a specific responsibility:

```
final-etl-project/
├── config.py           # Stores API keys and database configuration.
├── db_utils.py         # Handles database connection and schema retrieval.
├── nlp_to_sql.py       # Converts natural language queries to SQL.
├── extract.py          # Extracts data from the database.
├── transform.py        # Cleans and transforms the extracted data.
├── load.py             # Loads data into the final table.
├── main.py             # The main application entry point.
├── requirements.txt    # Lists all Python dependencies.
├── init.sql            # SQL script to create and populate the database.
└── ecommerce.db        # The SQLite database file (created on first run).
```

---

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

-   Python 3.8 or newer.
-   [DB Browser for SQLite](https://sqlitebrowser.org/dl/) (a free tool to manage the database).

### 2. Clone the Repository

If your project is on GitHub, clone it. Otherwise, simply ensure all the project files are in a single folder.

```bash
git clone [https://github.com/b-ravi-teja/etl-project.git](https://github.com/b-ravi-teja/etl-project.git)
cd final-etl-project  # Navigate into your refactored project folder
```

### 3. Install Dependencies

Open your terminal in the project root folder and run the following command to install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key

-   Open the `config.py` file.
-   Replace the placeholder text `"YOUR_GEMINI_API_KEY_HERE"` with your actual Gemini API key.

```python
# config.py
GEMINI_API_KEY = "AIzaSy...your...key...here..."
```

### 5. Create and Populate the Database (One-Time Setup)

The database is a single file (`ecommerce.db`) that the script will create. You need to create the tables and add data to it.

1.  **Run the Python script once** to create the empty database file:
    ```bash
    python main.py
    ```
    *(The script will create `ecommerce.db` and then likely warn you that the database is empty. This is expected.)*

2.  **Open DB Browser for SQLite**.

3.  Click **"Open Database"** and select the `ecommerce.db` file from your project folder.

4.  Go to the **"Execute SQL"** tab.

5.  Click the "Open SQL file" icon (a folder icon) and select your `init.sql` file.

6.  Click the blue "Execute all" button (▶) to run the script and create your tables.

7.  **IMPORTANT**: Click the **"Write Changes"** button to save the data to the file, then close the application.

---

## How to Run the Application

Once the setup is complete, you can run the main application from your terminal:

```bash
python main.py
```

The system will connect to the database and prompt you for your questions.

## How to Use

After launching the application, you can type your questions in plain English. The system works best with queries that require joining information across multiple tables.

**Example Queries:**

```
💬 Enter your query: Show all orders placed by Alice Johnson
```
💬 Enter your query: List all products from the Electronics category that have been ordered
```
💬 Enter your query: which customers ordered a Classic Cotton T-Shirt
```

After each query, the system will perform the full ETL process and save the results in the `final` table within your `ecommerce.db` database. You can view this table using DB Browser for SQLite to see the final reports. To exit the application, simply type `quit` or `exit`.
