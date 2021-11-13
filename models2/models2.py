from sqlalchemy import Column, Integer, Text
from models2.database2 import Base2

class mapContent(Base2):
    __tablename__ = 'mapcontents'
    id = Column(Integer, primary_key=True)
    map = Column(Text)

    def __init__(self, id=None, map=None):
        self.id = id
        self.map = map

    def __repr__(self):
        return '<Map %r>' % (self.map)