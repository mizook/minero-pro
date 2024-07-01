import os
import sys

import pandas as pd


class Utils:
    @staticmethod
    def get_resource_path(relative_path):
        """Get the absolute path to the resource, works for dev and for PyInstaller"""
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    @staticmethod
    def get_app_favicon():
        return Utils.get_resource_path("assets/minero-pro.svg")

    @staticmethod
    def get_github_icon():
        return Utils.get_resource_path("assets/github-icon.svg")

    @staticmethod
    def get_minero_pro_image():
        return Utils.get_resource_path("assets/minero-pro.svg")

    @staticmethod
    def read_coordinates(filename):
        df = pd.read_csv(
            filename, header=None, names=["X", "Y", "Z", "Tonelaje", "Metal", "Metal2"]
        )
        return df

    @staticmethod
    def get_mineplan(filename):
        df = pd.read_csv(filename, sep=",")
        df.columns = ["Period", "XIndex", "YIndex", "ZIndex"]
        return df

    @staticmethod
    def get_rock_type(XIndex, ZIndex):
        if ZIndex == 1 and (
            (XIndex <= 2)
            or (XIndex >= 6 and XIndex <= 9)
            or (XIndex >= 13 and XIndex <= 14)
            or (XIndex >= 18 and XIndex <= 19)
            or (XIndex >= 23 and XIndex <= 25)
            or (XIndex >= 29 and XIndex <= 30)
            or (XIndex >= 35)
        ):
            return "B"

        if ZIndex == 2 and (
            (XIndex <= 2)
            or (XIndex >= 6 and XIndex <= 8)
            or (XIndex >= 13 and XIndex <= 14)
            or (XIndex >= 18 and XIndex <= 19)
            or (XIndex >= 23 and XIndex <= 24)
            or (XIndex >= 29 and XIndex <= 30)
            or (XIndex >= 34)
        ):
            return "B"

        if ZIndex == 3 and (
            (XIndex <= 1)
            or (XIndex >= 5 and XIndex <= 8)
            or (XIndex >= 12 and XIndex <= 14)
            or (XIndex >= 17 and XIndex <= 18)
            or (XIndex >= 22 and XIndex <= 23)
            or (XIndex >= 28 and XIndex <= 29)
            or (XIndex >= 35)
        ):
            return "B"

        if ZIndex == 4 and (
            (XIndex <= 1)
            or (XIndex >= 5 and XIndex <= 7)
            or (XIndex >= 12 and XIndex <= 13)
            or (XIndex >= 17 and XIndex <= 18)
            or (XIndex >= 22 and XIndex <= 23)
            or (XIndex >= 27 and XIndex <= 28)
            or (XIndex >= 35)
        ):
            return "B"

        if ZIndex == 5 and (
            (XIndex >= 5 and XIndex <= 7)
            or (XIndex >= 11 and XIndex <= 13)
            or (XIndex >= 17 and XIndex <= 18)
            or (XIndex >= 22 and XIndex <= 23)
            or (XIndex >= 27 and XIndex <= 28)
            or (XIndex == 32)
            or (XIndex >= 35)
        ):
            return "B"

        if ZIndex == 6 and (
            (XIndex >= 4 and XIndex <= 6)
            or (XIndex >= 11 and XIndex <= 13)
            or (XIndex == 17)
            or (XIndex >= 21 and XIndex <= 22)
            or (XIndex >= 27 and XIndex <= 28)
            or (XIndex == 32)
            or (XIndex >= 35)
        ):
            return "B"

        if ZIndex == 7 and (
            (XIndex >= 4 and XIndex <= 5)
            or (XIndex >= 11 and XIndex <= 13)
            or (XIndex >= 16 and XIndex <= 17)
            or (XIndex >= 20 and XIndex <= 22)
            or (XIndex >= 26 and XIndex <= 27)
            or (XIndex == 31)
            or (XIndex == 35)
        ):
            return "B"

        if ZIndex == 8 and (
            (XIndex == 1)
            or (XIndex >= 3 and XIndex <= 5)
            or (XIndex == 7)
            or (XIndex >= 11 and XIndex <= 12)
            or (XIndex == 16)
            or (XIndex >= 20 and XIndex <= 21)
            or (XIndex >= 26 and XIndex <= 27)
            or (XIndex == 31)
            or (XIndex >= 34 and XIndex <= 35)
        ):
            return "B"

        if ZIndex == 9 and (
            (XIndex <= 6)
            or (XIndex >= 10 and XIndex <= 16)
            or (XIndex >= 19 and XIndex <= 22)
            or (XIndex >= 26 and XIndex <= 28)
            or (XIndex == 31)
            or (XIndex >= 34 and XIndex <= 35)
        ):
            return "B"

        if ZIndex == 10 and (
            (XIndex <= 4)
            or (XIndex >= 9 and XIndex <= 14)
            or (XIndex >= 19 and XIndex <= 20)
            or (XIndex >= 25 and XIndex <= 27)
            or (XIndex == 31)
            or (XIndex == 33)
        ):
            return "B"

        if ZIndex == 11 and (
            (XIndex <= 3)
            or (XIndex >= 8 and XIndex <= 13)
            or (XIndex >= 17 and XIndex <= 20)
            or (XIndex >= 24 and XIndex <= 26)
            or (XIndex >= 30 and XIndex <= 32)
        ):
            return "B"

        if ZIndex == 12:
            return "B"

        return "A"
