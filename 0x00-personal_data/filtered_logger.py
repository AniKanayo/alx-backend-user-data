#!/usr/bin/env python3

"""
filtered_logger.py
"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """
    Class RedactingFormatter

    Redacting Formatter class for filtering sensitive
    information in log messages.
    """
    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__("[HOLBERTON] \
            %(name)s %(levelname)s %(asctime)-15s: %(message)s")
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format function to filter sensitive information
        in log messages.

        Args:
            record: The LogRecord to be formatted.

        Returns:
            The formatted log message with filtered sensitive
            information.
        """
        message = self.filter_fields(record.msg)
        record.msg = message
        return super().format(record)

    def filter_fields(self, message: str) -> str:
        """
        Filter and redact specific fields in a log message.

        Args:
            message: The log message to be filtered.

        Returns:
            The filtered log message with redacted values for the
            specified fields.
        """
        for field in self.fields:
            pattern = fr"{field}=([^;]*)"
            message = re.sub(pattern, fr"{field}={self.REDACTION}", message)
        return message


def main() -> None:
    """
    Main function to demonstrate the usage of RedactingFormatter
    class.
    """
    # Create logger
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)

    # Create formatter
    formatter = RedactingFormatter(fields=["email", "ssn", "password"])

    # Create console handler and set formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add console handler to the logger
    logger.addHandler(console_handler)

    # Log a message
    logger.info("name=Bob; email=bob@example.com; ssn=123-45-6789;"
                " password=secret")

if __name__ == "__main__":
    main()
