import pyodbc

# Define connection parameters
server = 'your_server_name'   # e.g. 'localhost' or '127.0.0.1'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Create the connection string
conn_str = f"""
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
"""

try:
    # Establish the connection
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")

    # Create a cursor
    cursor = conn.cursor()

    # Example query
    cursor.execute("SELECT TOP 5 * FROM your_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connection
    conn.close()

except Exception as e:
    print("Error:", e)
