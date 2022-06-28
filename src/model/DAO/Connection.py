from src.model.DAO.Config import Config
import psycopg2 as db


class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.__conn = db.connect(**self.config["postgres"])
            self.__cur = self.__conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.commit()
        self.get_connection.close()

    @property
    def get_connection(self):
        return self.__conn

    @property
    def get_cursor(self):
        return self.__cur

    def commit(self):
        self.get_connection.commit()

    def fetchall(self):
        return self.get_cursor.fetchall()

    def execute(self, sql, params=None):
        self.get_cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.get_cursor.execute(sql, params or ())
        return self.fetchall()
