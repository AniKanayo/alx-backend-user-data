#!/usr/bin/env python3
"""
Module that defines the User SQLAlchemy model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model for the 'users' table in the database.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __init__(self, email: str, hashed_password: str,
                 session_id: str = None, reset_token: str = None):
        """
        Initialize a User object.

        :param email: The user's email address.
        :param hashed_password: The hashed password.
        :param session_id: The user's session ID (optional).
        :param reset_token: The password reset token (optional).
        """
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

    def __repr__(self):
        """
        Return a string representation of the User object.
        """
        return f"<User(id={self.id}, email={self.email})>"
