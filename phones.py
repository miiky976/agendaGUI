import sqlite3


class Database:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("agenda.db")
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
        CREATE TABLE IF NOT EXISTS agenda (
        id int PRIMARY KEY,
        nombre VARCHAR(50),
        producto VARCHAR(50),
        numero VARCHAR(20),
        precio int
        );
        """
        self.cursor.execute(sql_command)

    def insert(self, identity, nombre, producto, numero, precio):
        try:
            sql_command = f"""
                           INSERT INTO agenda (id, nombre, producto, numero, precio)
                           VALUES ("{identity}", "{nombre}", "{producto}", "{numero}", "{precio}");
                           """
            self.cursor.execute(sql_command)
            self.connection.commit()
        except Exception as err:
            self.connection.rollback()
            print("Could not add to database")
            print(err)

    def update(self, identity, nombre, producto, numero, precio):
        result = self.get_id(identity)
        if result:
            try:
                sql_command = """UPDATE agenda SET nombre = ?, producto = ?, numero = ?, precio = ? WHERE id = ?"""
                self.cursor.execute(sql_command, (nombre, producto, numero, precio, identity))
                self.connection.commit()
            except Exception as err:
                self.connection.rollback()
                print("Could not update table")
                print(err)

    def delete(self, identity):
        try:
            sql_command = """DELETE FROM agenda WHERE id = ?"""
            self.cursor.execute(sql_command, (identity,))
            self.connection.commit()
        except Exception as err:
            self.connection.rollback()
            print("Could not delete from table")
            print(err)

    def get_all(self):
        try:
            sql_command = 'SELECT * FROM agenda'
            self.cursor.execute(sql_command)
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)

    def get_id(self, value):
        try:
            sql_command = f'SELECT * FROM agenda WHERE id={value}'
            self.cursor.execute(sql_command)
            result = self.cursor.fetchall()
            return result[0]
        except Exception as err:
            print(err)

    def close(self):
        self.connection.close()
