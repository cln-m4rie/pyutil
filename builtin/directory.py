from pathlib import Path
try:
    from .printer import Printer
except ImportError:
    from printer import Printer


class Directory:
    from typing import Union

    @staticmethod
    def make(directory_path: Union[str, Path], clean: bool = False):
        """
        ディレクトリを作る
        Args:
            directory_path (str|Path): ディレクトリまでのフルパス
            clean (bool): ディレクトリ初期化
        """
        import shutil
        directory_path = Path(directory_path)

        created = True

        if clean:
            if directory_path.exists():
                shutil.rmtree(directory_path)

        if directory_path.exists():
            created = False
            Printer.warn(
                f'\'{directory_path}\' already exist')

        directory_path.mkdir(parents=True, exist_ok=True)

        if created:
            Printer.success(f'\'{directory_path}\' created.')

    @staticmethod
    def remove(directory_path: Union[str, Path]):
        """
        ディレクトリを削除する
        Args:
            directory_path (str|Path): ディレクトリまでのフルパス
        """
        import shutil
        directory_path = Path(directory_path)
        shutil.rmtree(directory_path)
        Printer.success(f'\'{directory_path}\' deleted.')
