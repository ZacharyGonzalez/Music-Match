from sql_connect import SQL_Handler
sql_handler = SQL_Handler()

sql_handler.check_connected()
sql_handler.close()