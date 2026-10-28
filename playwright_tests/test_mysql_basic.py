import os
import pymysql

def test_mysql_orders_count(mysql_db):
    cur = mysql_db.cursor()
    cur.execute("SELECT COUNT(*) FROM orders")
    assert cur.fetchone()[0] == 3


def test_mysql_customer_total(mysql_db):
    cur = mysql_db.cursor()
    cur.execute("SELECT SUM(Amount) FROM orders WHERE CustomerID = %s", (1,))
    assert cur.fetchone()[0] == 650

def test_mysql_item_of_order_104(mysql_db):
    cur = mysql_db.cursor()
    cur.execute("SELECT Item FROM orders WHERE OrderID = %s", (104,))
    assert cur.fetchone()[0] == "Burger"