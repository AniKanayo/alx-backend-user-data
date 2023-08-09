#!/usr/bin/env python3

import re
from typing import List, Any


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces field values in the given message with a redaction string.

    Args:
        fields (List[str]): a list of strings representing the fields to be
        obfuscated.
        redaction (str): a string representing the redaction used to
        replace the fields.
        message (str): a string representing the log message.
        separator (str): a string representing the character separating
        the fields in the message.

    Returns:
        The obfuscated message string.
    """
    for field in fields:
        message = re.sub(f"{field}={field}[^{separator}]*",
                         f"{field}={redaction}", message)
    return message
