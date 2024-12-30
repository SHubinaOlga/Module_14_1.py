import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance)'
                    'VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i *10}', f'1000'))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',(500, f'User{i}'))

for i in range(1, 22, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

cursor.execute('SELECT * FROM Users WHERE age != 60')

us = cursor.fetchall()
for user in us:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connection.commit()
connection.close()