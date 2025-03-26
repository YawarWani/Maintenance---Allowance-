import sqlite3

DATABASE = "database.db"

# Connect to the database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# ✅ Step 1: Fetch all table names dynamically
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [table[0] for table in cursor.fetchall()]

# ✅ Step 2: Read and display data from each table
for table in tables:
    print(f"\n=== 📌 Table: {table} ===")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    # Fetch column names for better readability
    columns = [description[0] for description in cursor.description]
    print(f"Columns: {columns}")

    # Print each row
    for row in rows:
        print(row)

# Close the connection
conn.close()
