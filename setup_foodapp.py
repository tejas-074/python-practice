import sqlite3

conn = sqlite3.connect("foodapp.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Orders")
cur.execute("DROP TABLE IF EXISTS Customers")
cur.execute("CREATE TABLE Customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT)")
cur.execute("CREATE TABLE Orders (id INTEGER PRIMARY KEY, customer_id INTEGER, item TEXT, amount INTEGER)")

cur.executemany("INSERT INTO Customers VALUES (?, ?, ?)",
                [(1, "Amit", "Surat"), (2, "Riya", "Pune"), (3, "Karan", "Mumbai")])
cur.executemany("INSERT INTO Orders VALUES (?, ?, ?, ?)",
                [(1, 1, "Pizza", 300), (2, 1, "Burger", 150), (3, 2, "Pasta", 250)])

conn.commit()

print(cur.execute("SELECT COUNT(*) FROM Customers").fetchone()[0],
      cur.execute("SELECT COUNT(*) FROM Orders").fetchone()[0])
conn.close()