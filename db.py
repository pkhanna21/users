import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='users_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
