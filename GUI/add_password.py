import sqlite3


def add_password_db(service, login, password):
    connection = sqlite3.connect('SXwTRV21F0lC.db')
    cursor = connection.cursor()


    cursor.execute('''
        INSERT INTO pssws(service, login, password) VALUES(?, ?, ?)
    ''', (service, login, password))
    connection.commit()
    connection.close()