import os
from snowflake.snowpark import Session


class Dadosfera:
    def __init__(self):
        # coletando credenciais do SnowFlake
        self.snowflake_user = "DADOSFERA_PRD_DADOSFERATECH"
        self.snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
        self.snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
        self.snowflake_warehouse = "COMPUTE_WH"
        self.snowflake_database = "DADOSFERA_PRD_DADOSFERATECH"
        self.snowflake_schema = "PUBLIC"

    def connect_to_snowflake(self):
        params = {
            "user": self.snowflake_user,
            "password": self.snowflake_password,
            "account": self.snowflake_account,
            "warehouse": self.snowflake_warehouse,
            "database": self.snowflake_database,
            "schema": self.snowflake_schema,
        }
        # criando uma conexão com o SnowFlake
        snowpark = Session.builder.configs(params).create()
        return snowpark

    def get_data_from_catalog(self, prefix: str, suffix: str, select=["*"], where=""):
        # função que recupera o sql do banco e retorna um dataframe
        snowpark = self.connect_to_snowflake()
        table = snowpark.read.table(f"{self.snowflake_schema}.{prefix}_{suffix}")
        if where:
            df = table.select(select).where(where)
        else:
            df = table.select(select)
        return df

    def get_data_with_sql(self, sql: str):
        snowpark = self.connect_to_snowflake()
        return snowpark.sql(sql)
