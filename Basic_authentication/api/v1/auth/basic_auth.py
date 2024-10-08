#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """ Basic Authentication Class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes the Base64 authorization header. """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts user email and password from Base64 decoded string."""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string at the first occurrence of ':'
        user_email, password = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, password

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve User instance based on Basic Authentication"""

        # Get Authorization header
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        # Extract Base64 part from the Authorization header
        base64_header = self.extract_base64_authorization_header(auth_header)
        if not base64_header:
            return None

        # Decode Base64 string
        decoded_credentials = self.decode_base64_authorization_header(
            base64_header)
        if not decoded_credentials:
            return None

        # Extract email and password from decoded credentials
        email, password = self.extract_user_credentials(decoded_credentials)
        if not email or not password:
            return None

        # Fetch the user using email and password
        user = self.user_object_from_credentials(email, password)
        return user
