import datetime
import logging
import os
import random
import time

from flask import Flask, render_template, request, Response
import sqlalchemy

# Hydrate the environment from the .env file
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

logger = logging.getLogger()

def init_db_connection():
    db_config = {
        'pool_size': 5,
        'max_overflow': 2,
        'pool_timeout': 30,
        'pool_recycle': 1800,
    }
    return init_unix_connection_engine(db_config)

def init_unix_connection_engine(db_config):
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            database=os.environ.get('DB_NAME'),
            query={"unix_socket": "/cloudsql/{}/rankstrategy-ce64c:us-central1:googlesql".format(os.environ.get(CLOUD_SQL_CONNECTION_NAME) }
        ),
        **db_config
    )
    pool.dialect.description_encoding = None
    return pool

db = init_db_connection()

@app.route('/', methods=['GET'])
def index():
 
    with db.connect() as conn:
        # Execute the query and fetch all results
        recent_votes = conn.execute(
            "SELECT  (select count(*) from dbo.Twitter ) AS Total_Twitter_ID,  (select count(*) from dbo.Twitter_Metrics ) AS Total_Twitter_Metrics"
        ).fetchall()
  

    return recent_votes
    )


@app.route('/', methods=['POST'])
def save_vote():
    # Get the team and time the vote was cast.
    return 'hi javad'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
