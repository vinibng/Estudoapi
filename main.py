from connector.dbfactory import get_database_engine
from connector.cartinha_dao import CartinhaDao
from flask import Flask
from controller.magic import cartinha_blueprint

app =Flask(__name__)
app.register_blueprint(cartinha_blueprint)

def main():
  engine = get_database_engine()
  CartinhaDao.migrate_table(engine)
  app.run()
  
if __name__ == "__main__":
  main()
