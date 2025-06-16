# -*- coding: utf-8 -*-"

"""
Core functions for task 02
"""

import re
from typing import Callable, Iterator


REAL_NUMBER_FIND_SPACES_BOUNDARIES_PATTERN = re.compile(r' [-+]?\d*\.?\d+? ')
REAL_NUMBER_FIND_WHITESPACES_BOUNDARIES_PATTERN = re.compile(r'\s[-+]?\d*\.?\d+?\s')
REAL_NUMBER_FIND_WORDS_BOUNDARIES_PATTERN = re.compile(r'\b[-+]?\d*\.?\d+?\b')


def generator_numbers_ext(boundaries: str = 'words') -> Callable[[str], Iterator[float]]:
    """Closure for the function that finds all real numbers with a given text

    :param boundaries: Boundaries for searching real numbers (string, mandatory)
    :return A function that finds all real numbers with a given text (Callable)
    """

    search_pattern = (
        REAL_NUMBER_FIND_SPACES_BOUNDARIES_PATTERN
        if boundaries.lower() == 'spaces' else
        (
            REAL_NUMBER_FIND_WHITESPACES_BOUNDARIES_PATTERN
            if boundaries.lower() == 'whitespaces' else
            REAL_NUMBER_FIND_WORDS_BOUNDARIES_PATTERN
        )
    )

    def _generator_numbers(text: str) -> Iterator[float]:
        """Search through the text to find all real numbers and return them one at a time using a generator

        :param text: Text in which need to find all real numbers (string, mandatory)
        :return The next real number found (Generator of float)
        """
        for match in re.finditer(search_pattern, text):
            yield round(float(match.group()), 2)

    return _generator_numbers


def generator_numbers(text: str) -> Iterator[float]:
    """Search through the text to find all real numbers and return them one at a time using a generator

    :param text: Text in which need to find all real numbers (string, mandatory)
    :return The next real number found (Generator of float)
    """
    for match in re.finditer(REAL_NUMBER_FIND_SPACES_BOUNDARIES_PATTERN, text):
        yield round(float(match.group()), 2)


def sum_profit(text: str, search_func: Callable[[str], Iterator[float]]) -> float:
    """Calculate and return the sum of all the real numbers produced by the specified function

    :param text: Text in which need to find all real numbers (string, mandatory)
    :param search_func: A function that searches for and returns all real numbers found in the given text (Callable, mandatory)
    :return The total of all real numbers found (float)
    """

    return sum(search_func(text))
