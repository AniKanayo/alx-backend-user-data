#!/usr/bin/env python3

"""
filtered_logger.py
"""

import re
from typing import List
import logging


class SensitiveDataFilter(logging.Filter):
    """
    Custom logging filter to redact sensitive information from log messages.
    """

    SENSITIVE_FIELDS = [
        "password",
        "date_of_birth"
    ]

    def filter(self, record: logging.LogRecord) -> bool:
        """
        Filter method to redact sensitive information from log messages.

        Args:
            record: The LogRecord to be filtered.

        Returns:
            True to allow the record to be processed, False to discard it.
        """
        message = record.getMessage()
        for field in self.SENSITIVE_FIELDS:
            message = re.sub(fr"{field}=([^;]*)", f"{field}=<REDACTED>",
                             message)
        record.msg = message
        return True


class RedactingFormatter(logging.Formatter):
    """
    Custom log formatter to filter and redact sensitive information
    in log messages.
    """

    def format(self, record: logging.LogRecord) -> str:
        """
        Format method to filter and redact sensitive information in log
        messages.

        Args:
            record: The LogRecord to be formatted.

        Returns:
            The formatted log message with filtered sensitive information.
        """
        if isinstance(record.msg, str):
            record.msg = self.redact(record.msg)
        return super().format(record)

    def redact(self, message: str) -> str:
        """
        Redact sensitive information in the log message.

        Args:
            message: The log message to be redacted.

        Returns:
            The redacted log message.
        """
        filter = SensitiveDataFilter()
        return filter.filter(message)


def main() -> None:
    """
    Main function to demonstrate the usage of RedactingFormatter class.
    """
    formatter = RedactingFormatter("[HOLBERTON] %(name)s \
        %(levelname)s %(asctime)-15s: %(message)s")
    logger = logging.getLogger("example")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    messages = [
        "name=egg;email=eggmin@eggsample.com;password=secret;"
        "date_of_birth=01/01/2000;",
        "name=bob;email=bob@dylan.com;password=123456;"
        "date_of_birth=02/02/2002;",
    ]

    for message in messages:
        logger.warning(message)


if __name__ == "__main__":
    main()
