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

    Redacting Formatter class for filtering sensitive information in
    log messages
    """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__("[HOLBERTON] %(name)s \
            %(levelname)s %(asctime)-15s: %(message)s")
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format function to filter sensitive information in log messages.

        Args:
            record: The LogRecord to be formatted.

        Returns:
            The formatted log message with filtered sensitive information.
        """
        message = super().format(record)
        for field in self.fields:
            message = self.filter_datum(field, self.REDACTION, message,
                                        self.SEPARATOR)
        return message

    @staticmethod
    def filter_datum(field: str, redaction: str, message: str,
                     separator: str = ";") -> str:
        """
        Filter and redact specific field in a log message.

        Args:
            field: The name of the field to be filtered.
            redaction: The string to be used as the redacted value.
            message: The log message to be filtered.
            separator: The separator used for separating fields in the
            log message.

        Returns:
            The filtered log message with redacted values for the specified
            field.
        """
        pattern = fr"{field}=([^{separator}]*)"
        replacement = fr"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
        return message


def main() -> None:
    """
    Main function to demonstrate the usage of RedactingFormatter
    class.
    """
    formatter = RedactingFormatter(fields=["password", "date_of_birth"])
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
