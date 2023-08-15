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
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure trailing slashes in path for consistency
        path += '/' if path[-1] != '/' else ''

        # Returns True if path is not in the list of excluded paths.
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Validate that request contains 'Authorization' header
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user.
        """
        return None   # Will be implemented later
