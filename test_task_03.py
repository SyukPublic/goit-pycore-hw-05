# -*- coding: utf-8 -*-"

"""
Tests for task 03
"""

import sys
from typing import Optional

from tasks.task_03 import load_logs, count_logs_by_level, display_log_counts, display_log_by_level


def main() -> None:
    try:
        log_file_path: Optional[str] = None
        log_level: Optional[str] = None

        # Check whether the script was run with a loga file and log level specified as an argument
        if len(sys.argv) > 1:
            # The script was run with at least one argument

            # Copy first argument value to the log file path
            log_file_path = sys.argv[1]

            if len(sys.argv) > 2:
                # Copy second optional argument value to the log level
                log_level = sys.argv[2]

        else:
            # The script was run without arguments – print the help string
            print(f"Usage:  {sys.argv[0]} <log file path> [log level]")
            exit(0)

        # Load the log data from a specified file
        logs = load_logs(log_file_path)

        # Print the empty line
        print()
        # Print the log line counts by level
        display_log_counts(count_logs_by_level(logs))

        if log_level:
            # Print the empty line
            print()
            # Print the log lines for the given level
            display_log_by_level(logs, log_level)


        # Print the empty line
        print()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
