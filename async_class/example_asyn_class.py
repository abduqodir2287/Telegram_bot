from db_sql.bot_class import helperDB
user = 20000404

base = helperDB("Universitet.db")
base.setup("Students")
base.add_item(user, 'Abduqodir2287')
print(base.select_item())
base.log_out()

