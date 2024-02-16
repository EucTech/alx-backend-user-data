#!/usr/bin/env python3
"""This is a clss for sessions"""
import base64
from uuid import uuid4
from typing import TypeVar

from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session Class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """created session function"""
        if user_id is None or not isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)
