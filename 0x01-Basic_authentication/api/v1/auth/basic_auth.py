#!/usr/bin/env python3
""" to manage the Basic API authentication.
"""

import base64
import email
from .auth import Auth
from models.base import Base
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ basic authentication class"""
    def __init__(self) -> None:
        """instant"""
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract based64 function"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None

        if authorization_header.startswith('Basic ') is False:
            return None
        else:
            parts = authorization_header.split(' ')
            return parts[1]


    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """ decode base64 function """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception as e:
            return None


    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """user object function"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for u in users:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None
