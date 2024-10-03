#!/usr/bin/env python3
"Personal data"
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message
