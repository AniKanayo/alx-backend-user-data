#!/usr/bin/env python3

"""
This module provides a function to filter and
redact specific fields in a log message.
"""

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.

    Args:
        fields: A list of field names to be redacted.
    """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Initialize RedactingFormatter.

        Args:
            fields: A list of field names to be redacted.
        """
        fmt = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: \
               %(message)s"
        super(RedactingFormatter, self).__init__(fmt)
        self.fields = fields

    def filter_datum(self, redaction: str, message: str) -> str:
        """
        Filter and redact specific fields in a log message.

        Args:
            redaction: The string to replace the field values with.
            message: The log message to be filtered.

        Returns:
            The filtered log message with redacted field values.
        """
        for field in self.fields:
            pattern = fr"{field}=([^{self.SEPARATOR}]*)"
            replacement = fr"{field}={redaction}"
            message = re.sub(pattern, replacement, message)
        return message

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record. Redact specific fields using filter_datum method.

        Args:
            record: The LogRecord to be formatted.

        Returns:
            The formatted log message with redacted fields.
        """
        original_message = super().format(record)
        return self.filter_datum(self.REDACTION, original_message)


def filter_datum(fields: List[str], redaction: str
                 message: str, separator: str = ';') -> str:
    """
    Filter and redact specific fields in a log message.

    Args:
        fields: A list of field names to be redacted.
        redaction: The string to replace the field values with.
        message: The log message to be filtered.
        separator: The character separating the fields in
                   the log message. Default is ';'.

    Returns:
        The filtered log message with redacted field values.
    """
    for field in fields:
        pattern = fr"{field}=([^{separator}]*)"
        replacement = fr"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
    return message


def main() -> None:
    """
    Main function to demonstrate the usage of filter_datum function.
    """
    fields = ["password", "date_of_birth"]
    redaction = "xxx"
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=secret;"
        "date_of_birth=01/01/2000;",
        "name=bob;email=bob@dylan.com;password=123456;"
        "date_of_birth=02/02/2002;"
    ]
    separator = ";"

    for message in messages:
        print(filter_datum(fields, redaction, message, separator))


if __name__ == "__main__":
    main()
