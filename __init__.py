# -*- coding: utf-8 -*-"

__title__ = 'Home Work 05'
__author__ = 'Roman'

from tasks.task_01 import caching_fibonacci
from tasks.task_02 import generator_numbers, generator_numbers_ext, sum_profit
from tasks.task_03 import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts, display_log_by_level
from tasks.task_04 import main as contacts_bot

__all__ = [
    'caching_fibonacci',
    'generator_numbers',
    'generator_numbers_ext',
    'sum_profit',
    'load_logs',
    'filter_logs_by_level',
    'count_logs_by_level',
    'display_log_counts',
    'display_log_by_level',
    'contacts_bot',
]
