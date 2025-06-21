# nlp_to_sql.py
# This module converts a natural language query into an intelligent SQL statement.

import requests
import json
from config import GEMINI_API_KEY

def convert_nlp_to_sql(user_query, schema):
    """
    Converts a natural language query to SQL, deciding whether to use the
    'final' table or join the source tables.
    """
    prompt = f"""
    You are an intelligent SQL query generator for a hybrid database system.
    Your job is to decide the most efficient way to answer the user's query.

    Here is the database schema:
    {schema}

    *** YOUR TASK ***
    Based on the user's query and the table descriptions, generate a single, executable SQLite query.

    *** DECISION LOGIC ***
    1.  **Check the 'final' table first.** If all the information the user is asking for (e.g., customer names, product categories, order dates) is available in the 'final' table, write a SIMPLE query against ONLY the 'final' table. This is the preferred, fastest method.
    2.  **If information is missing from 'final'**, then and only then, write a query that JOINS the necessary raw source tables (e.g., customers, products, reviews, etc.) to get the answer.

    *** EXAMPLES ***
    -   If the user asks "Show orders for Alice Johnson", you should query the 'final' table: `SELECT * FROM final WHERE customer_name = 'Alice Johnson';`
    -   If the user asks "Show all reviews for the Pro-Grade Laptop", you must join `reviews` and `products` because 'reviews' data is not in the 'final' table: `SELECT r.rating, r.comment FROM reviews r JOIN products p ON r.product_id = p.product_id WHERE p.name = 'Pro-Grade Laptop';`

    *** RULES ***
    -   Generate ONLY the raw SQL query. No explanations, no markdown.
    -   Use `LIKE` for case-insensitive string matching.

    Natural Language Query: {user_query}

    SQL Query:
    """
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"
        headers = {'Content-Type': 'application/json'}
        data = {"contents": [{"parts": [{"text": prompt}]}]}

        response = requests.post(url, headers=headers, json=data, timeout=20)
        response.raise_for_status()

        result = response.json()
        
        if 'candidates' in result and result['candidates']:
            sql_query = result['candidates'][0]['content']['parts'][0]['text'].strip()
        else:
            print("✗ Error: Gemini API did not return any candidates.")
            return None

        if sql_query.startswith('```sql'):
            sql_query = sql_query[6:]
        if sql_query.endswith('```'):
            sql_query = sql_query[:-3]
        
        return sql_query.strip()

    except Exception as e:
        print(f"✗ An unexpected error occurred in nlp_to_sql: {e}")
        return None
