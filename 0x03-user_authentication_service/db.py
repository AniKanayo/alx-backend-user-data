#!/usr/bin/env python3
"""
DB module
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False)
    hashed_password = Column(String(120), nullable=False)

    def __init__(self, email: str, hashed_password: str):
        self.email = email
        self.hashed_password = hashed_password


class DB:
    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def get_user(self, user_id: int) -> User:
        try:
            user = self._session.query(User).filter_by(id=user_id).one()
            return user
        except NoResultFound:
            return None

    def find_user_by(self, **kwargs) -> User:
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except (NoResultFound, InvalidRequestError):
            return None
