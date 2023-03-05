import sqlite3
#création de la class
class SqliteWrap:
    
    def __init__(self,nameDb=""):
        self.conn = sqlite3.connect(nameDb)
        self.cursor = self.conn.cursor()
    
    def create_table(self, tableName="", listFields = []):
        try:
            myCmd = f"CREATE TABLE {tableName}("
            for i in listFields:
                myCmd += f"{i[0]} {i[1]},"

            myCmd = myCmd[:-1] + ")"
            self.cursor.execute(myCmd)
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e

    def add_row(self,tableName="",listValue=[]):
        try:
            myCmd = f"INSERT INTO {tableName}("
            myValues = " VALUES ("
            for i in listValue:
                myCmd += f"'{i[0]}',"
                if type(i[1]) == str:
                    myValues += f"'{i[1]}',"
                else:
                    myValues += f"{i[1]},"

            myCmd = myCmd[:-1] + ")" + myValues[:-1] + ")"
            self.cursor.execute(myCmd)
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e
        
    def read_rows(self,tableName="", listFields=[]):
        try:
            myCmd = f"SELECT "
            for i in listFields:
                myCmd += i + ","

            myCmd = myCmd[:-1] + f" FROM {tableName}" 
            return self.cursor.execute(myCmd).fetchall(),None
        except Exception as e:
            return [],e
        
    def max_index(self,tableName="",field=""):
        try:
            myCmd = f"SELECT MAX({field}) FROM {tableName}"
            result =  self.cursor.execute(myCmd).fetchall()
            if result[0][0] == None:
                return [(0,)], None
            return result,None
        except Exception as e:
            return [],e
        
    def reset_table(self,tableName=""):
        try:
            self.cursor.execute(f"DELETE FROM {tableName}")
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e
        
    def delete_row(self,tableName="",condition=()):
        try:
            if type(condition[1]) == str:
                myCmd = f"DELETE FROM {tableName} WHERE {condition[0]} = '{condition[1]}'"
            else:
                myCmd = f"DELETE FROM {tableName} WHERE {condition[0]} = {condition[1]}"
            self.cursor.execute(myCmd)
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e
        
    def close_db(self):
        try:
            self.conn.commit()
            self.conn.close()
            return 1,None
        except Exception as e:
            return 0,e
       



