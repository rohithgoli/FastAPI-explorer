from sqlalchemy import Column, Integer, String
# from blog.database import Base


class Blog():
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class User():
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)