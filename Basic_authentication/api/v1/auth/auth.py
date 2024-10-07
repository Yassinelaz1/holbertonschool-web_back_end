#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for requiring authentication """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ will be the Flask request object """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
