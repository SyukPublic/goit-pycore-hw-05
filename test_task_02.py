# -*- coding: utf-8 -*-"

"""
Tests for task 02
"""


from tasks.task_02 import generator_numbers, generator_numbers_ext, sum_profit


def main() -> None:
    try:
        text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
        total_income = sum_profit(text, generator_numbers)
        print(f"Загальний дохід: {total_income}")
    except Exception as e:
        print(e)

    print()

    try:
        text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
        print("Загальний дохід: {total_income}".format(total_income=sum_profit(text, generator_numbers_ext('spaces'))))
        print("Загальний дохід: {total_income}".format(total_income=sum_profit(text, generator_numbers_ext('whitespaces'))))
        print("Загальний дохід: {total_income}".format(total_income=sum_profit(text, generator_numbers_ext())))
    except Exception as e:
        print(e)

    print()

    try:
        text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00"
        print("Загальний дохід: {total_income}".format(total_income=sum_profit(text, generator_numbers_ext('spaces'))))
        print("Загальний дохід: {total_income}".format(total_income=sum_profit(text, generator_numbers_ext('whitespaces'))))
        print("Загальний дохід: {total_income}".format(total_income=sum_profit(text, generator_numbers_ext())))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
