import sys

from currency_converter import CurrencyConverter

converter = CurrencyConverter()

start_info = "プログラムから出たい場合は「exit」を入力してください。"
input_info = "金額「ズウォティ」を入力してください： "
bye_info = "ご利用ありがとございました！"
wrong_info = "データは違います。"


def run():
    print(start_info)
    print()
    while True:
        user_input = input(input_info)
        if is_correct_exit(user_input):
            print(bye_info)
            sys.exit()
        elif is_number(user_input):
            print_result(user_input)
        else:
            print(wrong_info)


def is_correct_exit(text: str):
    return text.strip().lower() == "exit"


def is_number(num: str):
    return num.isnumeric()


def print_result(num: str):
    print(
        f"{num}ズウォティはおよそ{round(converter.convert(num, 'PLN', 'JPY'), 2)}円です"
    )


run()
