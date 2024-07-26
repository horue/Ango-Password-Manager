import sqlite3

def create_db():
    connection = sqlite3.connect('SXwTRV21F0lC.db')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS pssws(service TEXT NOT NULL, login TEXT NOT NULL, password TEXT NOT NULL)")

if __name__ == '__main__':
    create_db()