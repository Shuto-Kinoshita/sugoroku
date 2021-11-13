from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os


databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'map.db')
engine2 = create_engine('sqlite:///' + databese_file, convert_unicode=True)
db_session2 = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine2))
Base2 = declarative_base()
Base2.query = db_session2.query_property()

def init_db():
    import models2.models2
    Base2.metadata.create_all(bind=engine2)