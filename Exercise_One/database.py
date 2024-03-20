from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'user':  os.getenv('USER_NAME'),
    'password': os.getenv('PASSWORD'),
    'host': 'localhost',
    'database': os.getenv('DATABASE_NAME'),
}

Base = declarative_base()

engine_url = "mysql+mysqlconnector://%(user)s:%(password)s@%(host)s/%(database)s" % DB_CONFIG

def engine():
    engine = create_engine(url=engine_url, connect_args={'use_unicode': False})

    # Set pool_pre_ping for the engine
    from sqlalchemy.pool import QueuePool
    engine.poolclass = QueuePool
    engine.pool_pre_ping = True

    return engine