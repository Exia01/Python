# a cursor is the object we use to interact with the database
import pymysql.cursors
# Create a class that will give us an object that we can use to connect to a database
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',
        user = 'root',
        password = 'root',
        db = db,
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor, 
        autocommit = True,
        port = 8889)
        self.connection = connection
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:

                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
def connectToMySQL(db):
    return MySQLConnection(db)