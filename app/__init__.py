import os
import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

# Had to include the ODBC string in the code as environment variables were not working
# Despite the security risks involved with this, to maximize development time I have decided to risk exposing the string
params = urllib.parse.quote_plus(
    r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:flaskmd.database.windows.net,1433;Database=flaskmd;Uid=flaskmdadmin;Pwd={abcd1234!};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str, echo=True)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Wrap the Flask-Alchemy instance around the Flask Application
db = SQLAlchemy(app)

from app import routes

#setup the entire DB
@app.before_first_request
def create_tables():
    from app.models import Job
    db.drop_all()
    db.create_all()
