#!/usr/bin/env python3
""" This is User session class """
from models.base import Base


class UserSession(Base):
    """ This is user session class """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize od useer
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
