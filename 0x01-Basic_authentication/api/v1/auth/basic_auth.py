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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract user credentials function """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email = decoded_base64_authorization_header.split(":")[0]
        password = decoded_base64_authorization_header[len(email) + 1:]
        return (email, password)

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

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user function """
        au_head = self.authorization_header(request)
        if au_head is not None:
            cu_tok = self.extract_base64_authorization_header(au_head)
            if cu_tok is not None:
                decoded = self.decode_base64_authorization_header(cu_tok)
                if decoded is not None:
                    u_email, pword = self.extract_user_credentials(decoded)
                    if u_email is not None:
                        return self.user_object_from_credentials(
                            u_email, pword)
        return
