from idlelib.window import add_windows_to_menu
from turtledemo.penrose import start
from typing import Union
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config
import asyncpg



class Database:
    def __init__(self):
        self.pool: Union[Pool,None]=None
    async def create(self):
        self.pool=await asyncpg.create_pool(
            user=config.DB_USER,
            host=config.DB_HOST,
            database=config.DB_NAME,
            password=config.DB_PASS
        )
    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result =await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result= await connection.execute(command,*args)
            return result

    async def create_table_users(self):
        sql = """
           CREATE TABLE IF NOT EXISTS Users (
           id SERIAL PRIMARY KEY,
           full_name VARCHAR(255) NOT NULL,
           username varchar(255) NULL,
           telegram_id BIGINT NOT NULL UNIQUE 
           );
           """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_all_users_username(self):
        sql = "SELECT username FROM Users"
        return await self.execute(sql, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    # async  def create_table_users(self):
    #     sql="""
    #     CREATE TABLE IF NOT EXISTS tele_bot(
    #     id SERIAL PRIMARY KEY,
    #     full_name VARCHAR(225) NOT NULL,
    #     username VARCHAR(225) NULL,
    #     teleg_id BIGINT NOT NULL UNIQUE
    #     );
    #     """
    #     await self.execute(sql,execute=True)
    # @staticmethod
    # def format_args(sql, parameters: dict):
    #     sql += "AND".join([
    #         f"{item}=${num}" for num, item in enumerate(parameters.keys() ,
    #                                                     start=1)
    #     ])
    #     return sql, tuple(parameters.values())
    #
    # async def add_user(self, full_name, username, telegram_id):
    #     sql="INSERT INTO users (full_name,username,telegram_id) VALUES(1$, $2, $3) returning *"
    #     return await self.execute(sql,full_name,username,telegram_id, fetchrow=True)
    #
    # async def select_all_users(self):
    #     sql='SELECT * FROM tele_bot'
    #     return await self.execute(sql, fetch=True)
    #
    #
    # async def select_user(self, **kwargs):
    #     sql = "SELECT * FROM tele_bot WHERE "
    #     sql, parameters = self.format_args(sql, parameters=kwargs)
    #     return await self.execute(sql, *parameters, fetchrow=True)
    #
    # async  def count_users(self):
    #     sql="SELECT COUNT(*) FROM tele_bot"
    #     return await self.execute(sql,fetchval=True)
    #
    # async def update_user_username(self,username,telegram_id):
    #     sql="UPDATE tele_bot SET username=$1 WHERE telegram_id=$2"
    # async  def delet_useres(self):
    #     await self.execute("DELETE FROM tele_bot WHERE TRUE", execute=True)
    #
    # async def delete_user(self):
    #     await self.execute("DROP TABLE tele_bot", execute=True)
