import pytest
import sqlite3

def test_amit_orders_total():
    conn = sqlite3.connect("foodapp.db")
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM Orders WHERE customer_id = ?", (1,))
    total = cur.fetchone()[0]
    conn.close()
    assert total == 450

def test_riya_order_item():
    conn = sqlite3.connect("foodapp.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT Orders.item
        FROM Customers
        INNER JOIN Orders ON Customers.id = Orders.customer_id
        WHERE Customers.name = ?
    """, ("Riya",))
    item = cur.fetchone()[0]
    conn.close()
    assert item == "Pasta"

def test_customers_in_pune(db):
    row = db.execute("SELECT COUNT(*) FROM Customers WHERE city = ?", ("Pune",)).fetchone()
    assert row[0] == 1

def test_new_order_saved(db):
    db.execute("DELETE FROM Orders WHERE id = 99")
    db.execute("INSERT INTO Orders VALUES (?, ?, ?, ?)", (99, 3, "Noodles", 200))
    db.commit()

    row = db.execute("SELECT item, amount FROM Orders WHERE id = ?", (99,)).fetchone()
    assert row == ("Noodles", 200)

    db.execute("DELETE FROM Orders WHERE id = 99")
    db.commit()

def test_ui_count_matches_db(page, db):
    page.set_content("<p id='total'>Customers: 3</p>")
    ui_text = page.locator("#total").text_content()
    ui_count = int(ui_text.split(": ")[1])

    db_count = db.execute("SELECT COUNT(*) FROM Customers").fetchone()[0]
    assert ui_count == db_count

def test_orders_above_200(db):
    rows = db.execute("SELECT * FROM Orders WHERE amount > 200").fetchall()
    assert len(rows) == 2

def test_total_per_customer(db):
    rows = db.execute(
        "SELECT customer_id, SUM(amount) FROM Orders GROUP BY customer_id ORDER BY customer_id"
    ).fetchall()
    assert rows == [(1, 450), (2, 250)]

def test_customers_without_orders(db):
    rows = db.execute("""
        SELECT Customers.name
        FROM Customers
        LEFT JOIN Orders ON Customers.id = Orders.customer_id
        WHERE Orders.id IS NULL
    """).fetchall()
    assert rows == [(("Karan",))]

def test_average_order(db):
    avg = db.execute("SELECT ROUND(AVG(amount), 2) FROM Orders").fetchone()[0]
    assert avg == 233.33

def test_orders_from_surat(db):
    rows = db.execute("""
        SELECT item FROM Orders
        WHERE customer_id IN (SELECT id FROM Customers WHERE city = ?)
        ORDER BY item
    """, ("Surat",)).fetchall()
    assert rows == [("Burger",), ("Pizza",)]

def test_customers_with_many_orders(db):
    rows = db.execute("""
        SELECT customer_id, COUNT(*)
        FROM Orders
        GROUP BY customer_id
        HAVING COUNT(*) > 1
    """).fetchall()
    assert rows == [(1, 2)]

def test_most_expensive_order(db):
    row = db.execute("""
        SELECT item, amount
        FROM Orders
        ORDER BY amount DESC
        LIMIT 1
    """).fetchone()
    assert row == ("Pizza", 300)

def test_items_starting_with_p(db):
    rows = db.execute("""
        SELECT item FROM Orders
        WHERE item LIKE 'P%'
        ORDER BY item
    """).fetchall()
    assert rows == [("Pasta",), ("Pizza",)]

def test_distinct_customers(db):
    all_orders = db.execute("SELECT COUNT(customer_id) FROM Orders").fetchone()[0]
    people = db.execute("SELECT COUNT(DISTINCT customer_id) FROM Orders").fetchone()[0]
    assert all_orders == 3
    assert people == 2

def test_orders_between(db):
    rows = db.execute("""
        SELECT item FROM Orders
        WHERE amount BETWEEN 200 AND 300
        ORDER BY item
    """).fetchall()
    assert rows == [("Pasta",), ("Pizza",)]

def test_second_highest_order(db):
    amount = db.execute("""
        SELECT amount FROM Orders
        ORDER BY amount DESC
        LIMIT 1 OFFSET 1
    """).fetchone()[0]
    assert amount == 250

def test_big_spenders(db):
    rows = db.execute("""
        SELECT Customers.name, SUM(Orders.amount)
        FROM Customers
        INNER JOIN Orders ON Customers.id = Orders.customer_id
        GROUP BY Customers.name
        HAVING SUM(Orders.amount) > 300
    """).fetchall()
    assert rows == [("Amit", 450)]

def test_update_then_rollback(db):
    db.execute("UPDATE Orders SET amount = ? WHERE id = ?", (999, 1))
    changed = db.execute("SELECT amount FROM Orders WHERE id = 1").fetchone()[0]
    assert changed == 999

    db.rollback()
    original = db.execute("SELECT amount FROM Orders WHERE id = 1").fetchone()[0]
    assert original == 300

def test_customer_name_is_required(db):
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("INSERT INTO Customers VALUES (?, ?, ?)", (50, None, "Delhi"))

def test_duplicate_customer_id_refused(db):
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("INSERT INTO Customers VALUES (?, ?, ?)", (1, "Neha", "Delhi"))

def test_orders_per_customer(db):
    rows = db.execute("""
        SELECT Customers.name, COUNT(Orders.id)
        FROM Customers
        LEFT JOIN Orders ON Customers.id = Orders.customer_id
        GROUP BY Customers.name
        ORDER BY Customers.name
    """).fetchall()
    assert rows == [("Amit", 2), ("Karan", 0), ("Riya", 1)]