# nlp_to_sql.py
# Converts a natural language query to an SQL statement using the Gemini API.

import requests
import json
from config import GEMINI_API_KEY

def convert_nlp_to_sql(user_query, schema):
    """Converts a natural language query to SQL using the Gemini API."""
    prompt = f"""
    You are an expert SQL query generator for an e-commerce database.
    Your main task is to create a query that MERGES information from multiple tables based on the user's request.
    Convert the following natural language query into a single, executable SQLite statement.

    {schema}

    Rules:
    1. Generate ONLY the SQL query, without any explanations or markdown.
    2. ALWAYS use JOINs to connect tables like customers, orders, order_items, and products as needed to answer the query.
    3. Use the LIKE operator for case-insensitive text matching in SQLite.
    4. For safety, return only SELECT statements.
    5. Use clear and readable table aliases (e.g., c for customers, p for products).

    Natural Language Query: {user_query}

    SQL Query:
    """
    try:
        # Note: Using Gemini 1.5 Flash for speed and accuracy
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"
        headers = {'Content-Type': 'application/json'}
        data = {"contents": [{"parts": [{"text": prompt}]}]}

        response = requests.post(url, headers=headers, json=data, timeout=20)
        response.raise_for_status()

        result = response.json()
        sql_query = result['candidates'][0]['content']['parts'][0]['text'].strip()

        # Clean up potential markdown formatting
        if sql_query.startswith('```sql'):
            sql_query = sql_query[6:]
        if sql_query.endswith('```'):
            sql_query = sql_query[:-3]
        
        return sql_query.strip()

    except Exception as e:
        print(f"✗ Error calling Gemini API: {e}")
        return None
