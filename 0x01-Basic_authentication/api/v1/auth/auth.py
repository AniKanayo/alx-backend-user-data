#!/usr/bin/env python3
"""
Auth module for the API
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Auth class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to determine if path requires authentication.
        """
        return False  # Will be implemented later

    def authorization_header(self, request=None) -> str:
        """
        Method to get the value of the header request(Authorization).
        """
        return None  # Will be implemented later

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user.
        """
        return None   # Will be implemented later
