#!/usr/bin/env python3
""" User model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""Define the base class for declarative models"""
Base = declarative_base()


class User(Base):
    """SQLAlchemy model for the users table."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
