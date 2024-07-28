import sqlite3

def get_passwords():
    connection = sqlite3.connect('SXwTRV21F0lC.db')
    cursor = connection.cursor()

    cursor.execute('SELECT service, login, password FROM pssws')
    rows = cursor.fetchall()

    connection.close()
    return rows