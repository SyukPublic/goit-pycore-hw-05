# -*- coding: utf-8 -*-"

"""
Tests for task 03
"""

from pathlib import Path

from tasks.task_03 import load_logs


def main() -> None:
    try:
        # Test the relative path to the file
        logs = load_logs("./tasks/data/sample.log")
        print(logs)
    except Exception as e:
        print(e)

    try:
        # Test the absolute path to the file
        logs = load_logs(Path.cwd() / "./tasks/data/sample.log")
        print(logs)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
