#!/usr/bin/env python3
"""
Basic Auth module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
import binascii
from typing import TypeVar
from flask import request


class BasicAuth(Auth):
    """
    BasicAuth class to manage the API authentication.
    """

    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """
        Extract the Base64 part of the Authorization header for
        Basic Authentication.
        """
        if authorization_header is None or not \
                isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> s      return None, None
        user_email, user_password = \
            decoded_base64_authorization_header.split(':')
        return user_email, user_password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Return the User instance based on the provided user
        email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None users = User.search({"email": user_email})
        if len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    return self.user_object_from_credentials(user_email, user_pwd)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the User instance for a request using Basic
        Authentication.
        """
        if request is None:
            request = request
        authorization_header = self.authorization_header(request)

        if authorization_header is None:
            return None

        base64_authorization_header = \
            self.extract_base64_authorization_header(authorization_header)

        if base64_authorization_header is None:
            return None

        decoded_base64_authorization_header = \
            self.decode_base64_authorization_header
        (base64_authorization_header)
    if decoded_base64_authorization_header is None:
        return None

        user_email, user_pwd = \
            self.extract_user_credentials(decoded_base64_authorization_header)

        if user_email is None or user_pwd is None:
            return None
