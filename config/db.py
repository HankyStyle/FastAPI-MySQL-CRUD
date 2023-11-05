from sqlalchemy import create_engine, MetaData

meta = MetaData()

# connect to sql database
engine = create_engine("mysql://root:password@localhost:3306/members")
connection = engine.connect()
