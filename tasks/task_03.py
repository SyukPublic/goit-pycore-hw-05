# -*- coding: utf-8 -*-"

"""
Core functions for task 03
"""

import re
import datetime
from typing import Any, Union
from collections import Counter
from pathlib import Path

from .futil import get_absolute_path, read_text_file_by_line


# Regular expression pattern for parsing the log line
LOG_FILE_LEVELS = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', }
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


# Date and Time string formats
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'


def load_logs(file_path: Union[Path, str]) -> list[dict[str, Any]]:
    """Load the log from the given file

    :param file_path: specified log file path (str, Path, mandatory)
    :return: log data with row index for further sorting (list of dictionaries)
    """

    return [
        dict(row_index=rn, **parse_log_line(line))
        for rn,  line in read_text_file_by_line(get_absolute_path(file_path))
        if line
    ]


def parse_log_line(line: str) -> dict[str, Any]:
    """Parse the log into the log data dictionary

    :param line: the log line (str, mandatory)
    :return: log data (dictionary)
    """

    try:
        if match := re.match(LOG_FILE_LINE_PATTERN, line):
            return {
                k: (
                    datetime.datetime.strptime(v, DATE_FORMAT).date()
                    if k == 'date' else (
                        datetime.datetime.strptime(v, TIME_FORMAT).time()
                        if k == 'time' else
                        (v.upper() if k == 'level' else v)
                    )
                )
                for k, v in match.groupdict().items()
            }
        else:
            # The line does not meet the requirements or is corrupted
            # Raise exception to the upper level
            raise ValueError(f'The log line "{line}" is corrupted')
    except ValueError as e:
        # Exceptions handled by the previous level
        # Raise exception to the upper level
        raise e
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def filter_logs_by_level(logs: list[dict[str, Any]], level: str) -> list[dict[str, Any]]:
    """Filter the log lines by the given level

    :param logs: the log data (list of dictionaries, mandatory)
    :param level: the log level by which the data will be filtered (string, mandatory)
    :return: filtered and sorted log data (list of dictionaries)
    """

    try:
        # Verify if the log level is correct
        if level.upper() not in LOG_FILE_LEVELS:
            raise ValueError(f'The log level must in one of following values: {", ".join(LOG_FILE_LEVELS)}')

        # Filter the log lines by the given level
        level_logs: list[dict[str, Any]] = list(filter(lambda row: row.get('level') == level.upper(), logs))

        # Sort the log lines
        level_logs.sort(key=lambda row: row.get('row_index', 0))

        # Return the log lines
        return level_logs
    except ValueError as e:
        # Exceptions handled by the previous level
        # Raise exception to the upper level
        raise e
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def count_logs_by_level(logs: list[dict[str, Any]]) -> dict[str, int]:
    """Count the log lines by the log level

    :param logs: the log data (list of dictionaries, mandatory)
    :return: the total number of log lines counted across all levels in the log data (dictionary)
    """

    try:
        return dict(**Counter([row.get('level') for row in logs]))
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def display_log_counts(counts: dict[str, int]) -> None:
    """Print formatted information about the total number of log lines counted across all levels

    :param counts: the total number of log lines counted across all levels in the log data (dictionary, mandatory)
    """

    try:
        # Define the columns headers
        level_header: str = 'Рівень логування'
        quantity_header: str = 'Кількість'

        # Print the log counts header
        print(f'{level_header:<{len(level_header) + 1}}|{quantity_header:>{len(quantity_header) + 1}}')
        print(f'{"-" * (len(level_header) + 1)}|{"-" * (len(quantity_header) + 1)}')

        # Print the log counts data
        for level, quantity in counts.items():
            print(f'{level:<{len(level_header) + 1}}|{quantity:>{len(quantity_header) + 1}}')
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def display_log_by_level(logs: list[dict[str, Any]], level: str) -> None:
    """Display log rows filtered by the given level

    :param logs: the log data (list of dictionaries, mandatory)
    :param level: the log level by which the data will be filtered (string, mandatory)
    """

    try:
        # Print the header
        print(f'Деталі логів для рівня \'{level.upper()}\':')

        # Print the log lines for given level
        for row in filter_logs_by_level(logs, level):
            print(
                '{date} {time} - {message}'.format(
                    date=row.get('date').strftime(DATE_FORMAT),
                    time=row.get('time').strftime(TIME_FORMAT),
                    message=row.get('message'),
                )
            )
    except ValueError as e:
        # Exceptions handled by the previous level
        # Raise exception to the upper level
        raise e
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))
