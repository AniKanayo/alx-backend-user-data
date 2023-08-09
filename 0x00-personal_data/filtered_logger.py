#!/usr/bin/env python3

"""
This module provides a RedactingFormatter class
that redacts specific fields in log messages.
"""

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Initialize RedactingFormatter.

        Args:
            fields: A list of field names to be redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
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
        Format the log record. Redact specific fields using filter_datum method

        Args:
            record: The LogRecord to be formatted.

        Returns:
            The formatted log message with redacted fields.
        """
        # Get the original log message
        original_message = super().format(record)

        # Redact specific fields using filter_datum method
        redacted_message = self.filter_datum(redaction=self.REDACTION,
                                             message=original_message)

        # Return the redacted log message
        return redacted_message


def main() -> None:
    """
    Main function to demonstrate the usage of RedactingFormatter.
    """
    # Set up logging with the RedactingFormatter
    fields = ["password", "date_of_birth"]
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields))
    logger = logging.getLogger("example")
    logger.addHandler(handler)

    # Sample log messages
    logger.warning("name=egg;email=eggmin@eggsample.com;password=secret;"
                   "date_of_birth=01/01/2000;")
    logger.warning("name=bob;email=bob@dylan.com;password=123456;"
                   "date_of_birth=02/02/2002;")


if __name__ == "__main__":
    main()
