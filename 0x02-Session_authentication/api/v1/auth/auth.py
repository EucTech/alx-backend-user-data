#!/usr/bin/env python3
"""This is a class to manage the API authentication."""

from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require function"""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header function """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """current user function"""
        return None

    def session_cookie(self, request=None):
        """session cookies function"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
