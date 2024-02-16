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
        if not path.endswith('/'):
            path += '/'

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ authorization header function """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """current user function"""
        return None
