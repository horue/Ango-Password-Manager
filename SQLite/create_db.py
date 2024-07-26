import sqlite3

def create_db():
    connection = sqlite3.connect('SXwTRV21F0lC.db')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS pssws(service, login, password)")

if __name__ == '__main__':
    create_db()