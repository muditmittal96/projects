import luigi
import luigi.contrib.mysqldb
from luigi.contrib import mysqldb
import pandas as pd
import mysql.connector
from mysql.connector import errorcode, Error


class InsertintoDictionary(mysqldb.CopyToTable):

    df = pd.read_csv("BankChurners.csv")
    host = "localhost"
    database = "testdb"
    user = "root"
    password = "mudit"
    table = "users3"
    update_id = "check7"

    def output(self):
       
        return mysqldb.MySqlTarget (
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            table=self.table,
            update_id=self.update_id

        )

    def rows(self):
        for index, row in self.df.iterrows():
            yield row
    
    def copy(self, cursor, file=None):

        query = "INSERT INTO users3 (CLIENTNUM, Customer_Age, Gender, Dependent_count, Education_Level, Marital_Status, Income_Category, Card_Category, Months_on_book, Total_Relationship_Count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        rows = []

        for idx, row in enumerate(self.rows()):
            rows.append(row)

            if (idx + 1) % self.bulk_size == 0:
                cursor.executemany(query, rows)
                rows = []

        cursor.executemany(query, rows)


    def run(self):

        connection = self.output().connect()
        cursor = connection.cursor()
        self.init_copy(connection)
        self.copy(cursor)
        # self.post_copy(connection)
        # if self.enable_metadata_columns:
        #     self.post_copy_metacolumns(cursor)
           

        self.output().touch(connection)
        connection.commit()
        connection.close()
    
    @property
    def bulk_size(self):
        return 15000


class InsertData(luigi.Task):

    def requires(self):
        yield InsertintoDictionary()


if __name__ == '__main__':
    
    env_params = {'local_scheduler': True,}
    task = InsertData()
    luigi.build([task], **env_params)