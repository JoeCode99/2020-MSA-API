import os
import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

# os.environ['dbstring']
db_string = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:flaskmd.database.windows.net,1433;Database=flaskmd;Uid=flaskmdadmin;Pwd={Dadisno1};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
params = urllib.parse.quote_plus(db_string)

params = urllib.parse.quote_plus \
(r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:flaskmd.database.windows.net,1433;Database=flaskmd;Uid=flaskmdadmin;Pwd={Dadisno1};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str,echo=True)

# initialization
#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'supersecret'
#app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Wrap our Flask-Alchemy instance around our Flask Application
db = SQLAlchemy(app)



from app import routes

@app.before_first_request
def create_tables():
    from app.models import Task
    db.drop_all()
    db.create_all()