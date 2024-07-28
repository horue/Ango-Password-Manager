import sqlite3


def add_password_db(service, login, password):
    connection = sqlite3.connect('SXwTRV21F0lC.db')
    cursor = connection.cursor()


    cursor.execute('''
        INSERT INTO pssws(service, login, password) VALUES(?, ?, ?)
    ''', (service, login, password))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    add_password_db(service='YT',login='email',password='senha')
    add_password_db(service='KR',login='e',password='ef')