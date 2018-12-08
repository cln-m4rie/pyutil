import datetime
from functools import partial


class Printer:
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'

    @staticmethod
    def print_colored(code, key, text, is_bold=True):
        if is_bold:
            code = '1;%s' % code

        print(
            f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] \033[{code}m{key}\033[0m: {text}')

    @staticmethod
    def info(text, is_bold=True):
        p = partial(
            Printer.print_colored,
            Printer.BLUE,
            'INFO'
        )
        p(text, is_bold)

    @staticmethod
    def success(text, is_bold=True):
        p = partial(
            Printer.print_colored,
            Printer.GREEN,
            'SUCCESS'
        )
        p(text, is_bold)

    @staticmethod
    def warn(text, is_bold=True):
        p = partial(
            Printer.print_colored,
            Printer.YELLOW,
            'WARNING'
        )
        p(text, is_bold)

    @staticmethod
    def error(text, is_bold=True):
        p = partial(
            Printer.print_colored,
            Printer.RED,
            'ERROR'
        )
        p(text, is_bold)

    @staticmethod
    def magenta(key, text, is_bold=True):
        p = partial(
            Printer.print_colored,
            Printer.MAGENTA)
        p(key, text, is_bold)

    @staticmethod
    def cyan(key, text, is_bold=True):
        p = partial(
            Printer.print_colored,
            Printer.CYAN)
        p(key, text, is_bold)

    @staticmethod
    def white(key, text, is_bold=True):
        p = partial(
            Printer.print_colored,
            Printer.WHITE)
        p(key, text, is_bold)
