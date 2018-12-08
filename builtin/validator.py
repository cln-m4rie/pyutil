import re
from typing import Union


class Validator:

    @staticmethod
    def exist(val=None):
        return True if val else False

    @staticmethod
    def is_zen(val: str) -> bool:
        """
        全てが全角文字か
        Args:
            val:
        Returns:
            bool
        """
        return True if re.match(
            r'^[^\x01-\x7E\xA1-\xDF]+$', val) else False

    @staticmethod
    def is_hira(val: str) -> bool:
        """
        全てが平仮名か
        Args:
            val (str):

        Returns:
            bool
        """
        return True if re.match(
            r'^[\u3041-\u3096]+$', val) else False

    @staticmethod
    def is_kana(val: str) -> bool:
        """
        全てが片仮名か
        Args:
            val (str):

        Returns:
            bool
        """
        return True if re.match(
            r'^[\u30a1-\u30f6]+$', val) else False

    @staticmethod
    def is_upper_alphabet(val: str) -> bool:
        """
        全てが大文字の英字か
        Args:
            val (str):

        Returns:
            bool
        """
        return True if re.match(
            r'^[A-Z]+$', val) else False

    @staticmethod
    def is_lower_alphabet(val: str) -> bool:
        """
        全てが小文字の英字か
        Args:
            val (str):

        Returns:
            bool
        """
        return True if re.match(
            r'^[a-z]+$', val) else False

    @staticmethod
    def is_alphabet(val: str) -> bool:
        """
        全てが(大小問わず)英字か
        Args:
            val (str):

        Returns:
            bool
        """
        return True if re.match(
            r'^[a-zA-Z]+$', val) else False

    @staticmethod
    def is_alphanumeric(val: Union[int, str]) -> bool:
        """
        全てが半角英数字か
        Args:
            val (str):

        Returns:
            bool
        """
        return True if isinstance(
            val, str) and re.match(
            r'^[0-9a-zA-Z]+$', val) else False

    @staticmethod
    def is_numeric(val: Union[int, str])->bool:
        """
        全てが半角数字か
        Args:
            val (int, str):

        Returns:
            bool
        """
        return True if re.match(r'^[0-9]+$', val) else False
