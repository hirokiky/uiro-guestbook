import datetime

import sqlalchemy as sa
from uiro.db import Base, Session


class Greeting(Base):
    __tablename__ = 'page'
    query = Session.query_property()
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    content = sa.Column(sa.String)
    ctime = sa.Column(sa.DateTime, default=datetime.datetime.now)

    def __init__(self, name, content):
        self.name = name
        self.content = content
