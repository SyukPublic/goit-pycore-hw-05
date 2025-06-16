# -*- coding: utf-8 -*-"

"""
Tests for task 01
"""

from tasks.task_01 import caching_fibonacci


def main() -> None:
    try:
        # Отримуємо функцію fibonacci
        fib = caching_fibonacci()

        # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
        print(fib(10))  # Виведе 55
        print(fib(15))  # Виведе 610
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
