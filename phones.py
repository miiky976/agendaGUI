import sqlite3


class Database:
    def __init__(self):
        try:
            self.phone_data = ""
            self.connection = sqlite3.connect("phonebook.db")
            self.cursor = self.connection.cursor()
            self.create_table()
        except Exception as e:
            print(e)
        else:
            print("Opened database successfully")
        finally:
            print("Finished Connecting to Database")

    def drop_table(self, table):
        sql_command = f"""DROP TABLE {table}"""
        self.cursor.execute(sql_command)

    def create_table(self):
        sql_command = """
        CREATE TABLE IF NOT EXISTS phonebook (
        id int PRIMARY KEY,
        fname VARCHAR(50),
        lname VARCHAR(50),
        number VARCHAR(20)
        );
        """
        self.cursor.execute(sql_command)

    def insert(self, identity, fname, lname, phone):
        try:
            sql_command = f"""
                           INSERT INTO phonebook (id, fname, lname, number)
                           VALUES ("{identity}", "{fname}", "{lname}", "{phone}");
                           """
            self.cursor.execute(sql_command)
            self.connection.commit()
        except Exception as err:
            self.connection.rollback()
            print("Could not add to database")
            print(err)

    def update(self, identity, fname, lname, phone):
        result = self.get_id(identity)
        if result:
            try:
                sql_command = """UPDATE phonebook SET fname = ?, lname = ?, number = ?\
                                 WHERE id = ?"""
                self.cursor.execute(sql_command, (fname, lname, phone, identity))
                self.connection.commit()
            except Exception as err:
                self.connection.rollback()
                print("Could not update table")
                print(err)

    def delete(self, identity):
        try:
            sql_command = """DELETE FROM phonebook WHERE id = ?"""
            self.cursor.execute(sql_command, (identity,))
            self.connection.commit()
        except Exception as err:
            self.connection.rollback()
            print("Could not delete from table")
            print(err)

    def get_all(self):
        try:
            sql_command = 'SELECT * FROM phonebook'
            self.cursor.execute(sql_command)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)

    def get_id(self, value):
        try:
            sql_command = f'SELECT * FROM phonebook WHERE id={value}'
            self.cursor.execute(sql_command)
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            print(err)

    def close(self):
        self.connection.close()
