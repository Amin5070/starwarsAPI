"""
user: root
password: qwerty
host: 127.0.0.1
port: 3306
database: starwarsDB
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='Amin5070',
                             port=3306,
                             password='Amin@5070',
                             database='starwarsDB',
                             cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()
cursor.execute("SHOW DATABASES")
results=cursor.fetchall()
for result in results:
    print (result)