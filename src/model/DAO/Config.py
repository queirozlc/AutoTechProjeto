import psycopg2 as db


class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "admin",
                "host": "localhost",
                "port": "5432",
                "database": "autotech"
            }
        }
