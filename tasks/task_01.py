# -*- coding: utf-8 -*-"

"""
Core functions for task 01
"""

from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """Create and return a function that computes the Fibonacci number using an internal cache

    :return pointer to the function that calculates the Fibonacci number (Callable)
    """

    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """Compute, cache and return the Fibonacci number

        :param n: the value for which the Fibonacci number will be calculated. (int, mandatory)
        :return calculated Fibonacci number (Callable)
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            nonlocal cache
            cache[n] =  fibonacci(n - 1) + fibonacci(n - 2)
            return cache.get(n, 0)

    return fibonacci
