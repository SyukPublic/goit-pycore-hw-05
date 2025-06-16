# -*- coding: utf-8 -*-"

"""
Core functions for task 03
"""

import re
from typing import Union
from pathlib import Path

from .futil import get_absolute_path, read_text_file_by_line


LOG_FILE_LEVELS = {r'DEBUG', r'INFO', r'WARNING', r'ERROR', }
YEAR_PATTERN = r'(?:\d{4})'
MONTH_NUMBER_PATTERN = r'(?:0[1-9]|1[0-2])'
MONTH_DAY_PATTERN = r'(?:0[1-9]|[12][0-9]|3[01])'
HOUR_PATTERN = r'(?:2[0123]|[01][0-9])'
MINUTE_PATTERN = r'(?:[0-5][0-9])'
SECOND_PATTERN = r'(?:[0-5][0-9]|60)'
LOG_FILE_LINE_PATTERN = re.compile(
    r'^(?P<date>{date})[ \t]+(?P<time>{time})[ \t]+(?P<level>{log_levels})[ \t]+(?P<message>.*)$'.format(
        date=rf'{YEAR_PATTERN}-{MONTH_NUMBER_PATTERN}-{MONTH_DAY_PATTERN}',
        time=rf'{HOUR_PATTERN}:{MINUTE_PATTERN}:{SECOND_PATTERN}',
        log_levels='|'.join(LOG_FILE_LEVELS),
    )
)


def load_logs(log_file_path: Union[Path, str]) -> list[dict]:

    return [parse_log_line(line) for line in read_text_file_by_line(get_absolute_path(log_file_path))]


def parse_log_line(log_line: str) -> dict:
    try:
        if match := re.match(LOG_FILE_LINE_PATTERN, log_line):
            return match.groupdict()
        else:
            raise ValueError('The log line is corrupted')
    except Exception as e:
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))
