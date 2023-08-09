#!/usr/bin/env python3

"""
This module provides a function to filter and redact
specific fields in a log message.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str = ';') -> str:
    """
    Filter and redact specific fields in a log message.

    Args:
        fields: A list of field names to be redacted.
        redaction: The string to replace the field values with.
        message: The log message to be filtered.
        separator: The character separating the fields in the log
        message. Default is ';'.

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
